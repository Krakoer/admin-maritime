#! /usr/bin/env python3

from flask import Flask, render_template, session, request, redirect, url_for, flash
import caldera
import testbed
import time

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/simulation", methods=["POST", "GET"])
def simu():
    if request.method == "GET":
        return render_template("simulation.html")
    elif request.method == "POST":
        data = request.form.to_dict(flat=False)
        # Process the data
        try:
            longi = float(data['long'][0])
            lat = float(data['lat'][0])
            poids = int(data['poidsNavire'][0][-1])
            attack = data['attaque'][0]
            others = data["others"][0]
            delai = int(data['delai'][0])
        except Exception as e:
            flash(e)

        # Get simu and ecdis agent
        cookie = caldera.auth()
        agents = caldera.get_agents(cookie)
        if "agents" in session:
            agents_roles = session["agents"]
            try:
                # https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
                paw_simu = list(agents_roles.keys())[list(agents_roles.values()).index("simu")]
                simu_agent = agents[paw_simu]
            except ValueError:
                flash("Aucun n'agent n'est enregistré en tant que simulateur")
                return redirect(url_for("simu"))
            if attack != 'none' or others != "none":
                try:
                    paw_ecdis = list(agents_roles.keys())[list(agents_roles.values()).index("ecdis")]
                    ecdis_agent = agents[paw_ecdis]
                except ValueError:
                    flash("Aucun n'agent n'est enregistré en tant qu'ECDIS")
                    return redirect(url_for("simu"))

        
            # Create simu command
            simu_command = testbed.run_simu(poids, longi, lat)

            # Create attack command
            attack_command = ""
            other_command  = ""
            if attack != 'none':
                attack_command = testbed.run_attack(attack, "")
            if others != 'none':
                other_command = testbed.run_others(others, "")
            # Run everything
            op_id = caldera.create_op("attack", cookie)
            caldera.run_command(simu_command, cookie, op_id, simu_agent.platform, simu_agent.paw)
            time.sleep(delai)
            if attack_command:
                caldera.run_command(attack_command, cookie, op_id, ecdis_agent.platform, ecdis_agent.paw)
            op_id = caldera.create_op("others", cookie)
            if other_command:
                caldera.run_command(other_command, cookie, op_id, ecdis_agent.platform, ecdis_agent.paw)
        else:
            flash("Aucun agent n'a de rôle enregistré")

        return redirect(url_for("simu"))

@app.route("/agents", methods=["POST", "GET"])
def agents():
    # Clear cached agents ID
    #session.clear()

    if request.method == "GET":
        cookie = caldera.auth()
        agents = caldera.get_agents(cookie)
        if 'agents' in session:
            for agent_paw, role in session["agents"].items():
                print(f"getting {agent_paw}: {role}")
                try:
                    agents[agent_paw].role = role
                except Exception as e:
                    print("# Error getting agent:" + str(e))
                    session["agents"].pop(agent_paw)
        return render_template("agents.html", agents=list(agents.values()))
    elif request.method == "POST":
        roles = request.form.to_dict(flat=False)
        session['agents'] = {}
        for paw, role in roles.items():
            role = role[0]
            session['agents'][paw] = role
            print(f"setting {paw}: {role}")
        return redirect(url_for("agents"))

if __name__=="__main__":
    app.run()
