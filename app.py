from flask import Flask, render_template, session, request, redirect, url_for
import caldera

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/simulation")
def simu():
    return render_template("simulation.html")

@app.route("/agents", methods=["POST", "GET"])
def agents():
    if request.method == "GET":
        cookie = caldera.auth()
        agents = caldera.get_agents(cookie)
        if 'agents' in session:
            for agent_paw, role in session["agents"].items():
                print(f"getting {agent_paw}: {role}")
                agents[agent_paw].role = role
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