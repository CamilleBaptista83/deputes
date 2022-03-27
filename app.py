from flask import Flask, render_template
import requests
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io
import base64

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        response = requests.get('https://www.nosdeputes.fr/synthese/data/json')
        deputes = response.json()["deputes"]
        return render_template('pages/home.html', deputes=deputes)

    @app.route("/selected/<int:id>/<prenom>/<nom>")
    def depute_selected(id, nom, prenom):
        nom_complet = nom.lower() + '-' + prenom.lower()
        response = requests.get('https://www.nosdeputes.fr/synthese/data/json')
        deputes = response.json()["deputes"]

        presence_depute_mois = {
            "octobre_2021": {},
            "novembre_2021": {},
            "decembre_2021": {},
            "janvier_2021": {},
            "fevrier_2021": {}
        }
        presence_depute_mois["octobre_2021"] = requests.get('https://www.nosdeputes.fr/synthese/202110/json')
        presence_depute_mois["octobre_2021"] = presence_depute_mois["octobre_2021"].json()["deputes"][1 - id]['depute'][
            'commission_presences']
        presence_depute_mois["novembre_2021"] = requests.get('https://www.nosdeputes.fr/synthese/202111/json')
        presence_depute_mois["novembre_2021"] = \
        presence_depute_mois["novembre_2021"].json()["deputes"][1 - id]['depute'][
            'commission_presences']
        presence_depute_mois["decembre_2021"] = requests.get('https://www.nosdeputes.fr/synthese/202112/json')
        presence_depute_mois["decembre_2021"] = \
        presence_depute_mois["decembre_2021"].json()["deputes"][1 - id]['depute'][
            'commission_presences']
        presence_depute_mois["janvier_2021"] = requests.get('https://www.nosdeputes.fr/synthese/202001/json')
        presence_depute_mois["janvier_2021"] = presence_depute_mois["janvier_2021"].json()["deputes"][1 - id]['depute'][
            'commission_presences']
        presence_depute_mois["fevrier_2021"] = requests.get('https://www.nosdeputes.fr/synthese/202002/json')
        presence_depute_mois["fevrier_2021"] = presence_depute_mois["fevrier_2021"].json()["deputes"][1 - id]['depute'][
            'commission_presences']

        df_mois = pd.DataFrame(presence_depute_mois, index=['presence_depute_mois']).T

        img = io.BytesIO()

        array = df_mois['presence_depute_mois'].to_numpy()
        sns.relplot(data=df_mois, kind="line", height=8.27)
        plt.yticks(range(0, max(array)+1, 1))
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)

        plot_url = base64.b64encode(img.getvalue()).decode('utf8')

        image = 'https://www.nosdeputes.fr/depute/photo/' + nom_complet + '/100'

        return render_template('pages/depute_selected.html', deputes=deputes, depute_selected=id, image=image,
                               plot_url=plot_url)

    @app.route("/groupe-politique")
    def groupe_politique():
        response = requests.get('https://www.nosdeputes.fr/synthese/data/json')
        deputes = response.json()["deputes"]

        differents_partis = {
            "groupe_politique": [
                {"name": "LREM", "keyword": "lrem"},
                {"name": "LR", "keyword": "lr"},
                {"name": "LFI", "keyword": "lfi"},
                {"name": "GDR", "keyword": "gdr"},
                {"name": "SOC", "keyword": "soc"},
                {"name": "LT", "keyword": "lt"},
                {"name": "MODEM", "keyword": "modem"},
                {"name": "AE", "keyword": "ae"},
                {"name": "UDI", "keyword": "udi"},
                {"name": "NI", "keyword": "ni"},
            ]

        }

        dataPartiPolitique = {
            'lr': {
                "nb_gens": 0,
                "hemicycle_presence": 0,
                "hemicycle_interventions": 0,
                "hemicycle_questions_orales": 0,
                "hemicycle_questions_ecrites": 0,
                "commission_presences": 0,
                "commission_interventions": 0,
                "rapports": 0,
                "propositions_ecrites": 0,
                "propositions_signees": 0,
                "amendements": 0,
                "moyenne_presence_commission": 0,
                "moyenne_presence_assemblee": 0,
            },
            'lrem': {
                "nb_gens": 0,
                "hemicycle_presence": 0,
                "hemicycle_interventions": 0,
                "hemicycle_questions_orales": 0,
                "hemicycle_questions_ecrites": 0,
                "commission_presences": 0,
                "commission_interventions": 0,
                "rapports": 0,
                "propositions_ecrites": 0,
                "propositions_signees": 0,
                "amendements": 0,
                "moyenne_presence_commission": 0,
                "moyenne_presence_assemblee": 0,
            },
            'lfi': {
                "nb_gens": 0,
                "hemicycle_presence": 0,
                "hemicycle_interventions": 0,
                "hemicycle_questions_orales": 0,
                "hemicycle_questions_ecrites": 0,
                "commission_presences": 0,
                "commission_interventions": 0,
                "rapports": 0,
                "propositions_ecrites": 0,
                "propositions_signees": 0,
                "amendements": 0,
                "moyenne_presence_commission": 0,
                "moyenne_presence_assemblee": 0,
            },
            'gdr': {
                "nb_gens": 0,
                "hemicycle_presence": 0,
                "hemicycle_interventions": 0,
                "hemicycle_questions_orales": 0,
                "hemicycle_questions_ecrites": 0,
                "commission_presences": 0,
                "commission_interventions": 0,
                "rapports": 0,
                "propositions_ecrites": 0,
                "propositions_signees": 0,
                "amendements": 0,
                "moyenne_presence_commission": 0,
                "moyenne_presence_assemblee": 0,
            },
            'soc': {
                "nb_gens": 0,
                "hemicycle_presence": 0,
                "hemicycle_interventions": 0,
                "hemicycle_questions_orales": 0,
                "hemicycle_questions_ecrites": 0,
                "commission_presences": 0,
                "commission_interventions": 0,
                "rapports": 0,
                "propositions_ecrites": 0,
                "propositions_signees": 0,
                "amendements": 0,
                "moyenne_presence_commission": 0,
                "moyenne_presence_assemblee": 0,
            },
            'lt': {
                "nb_gens": 0,
                "hemicycle_presence": 0,
                "hemicycle_interventions": 0,
                "hemicycle_questions_orales": 0,
                "hemicycle_questions_ecrites": 0,
                "commission_presences": 0,
                "commission_interventions": 0,
                "rapports": 0,
                "propositions_ecrites": 0,
                "propositions_signees": 0,
                "amendements": 0,
                "moyenne_presence_commission": 0,
                "moyenne_presence_assemblee": 0,
            },
            'modem': {
                "nb_gens": 0,
                "hemicycle_presence": 0,
                "hemicycle_interventions": 0,
                "hemicycle_questions_orales": 0,
                "hemicycle_questions_ecrites": 0,
                "commission_presences": 0,
                "commission_interventions": 0,
                "rapports": 0,
                "propositions_ecrites": 0,
                "propositions_signees": 0,
                "amendements": 0,
                "moyenne_presence_commission": 0,
                "moyenne_presence_assemblee": 0,
            },
            'ae': {
                "nb_gens": 0,
                "hemicycle_presence": 0,
                "hemicycle_interventions": 0,
                "hemicycle_questions_orales": 0,
                "hemicycle_questions_ecrites": 0,
                "commission_presences": 0,
                "commission_interventions": 0,
                "rapports": 0,
                "propositions_ecrites": 0,
                "propositions_signees": 0,
                "amendements": 0,
                "moyenne_presence_commission": 0,
                "moyenne_presence_assemblee": 0,
            },
            'udi': {
                "nb_gens": 0,
                "hemicycle_presence": 0,
                "hemicycle_interventions": 0,
                "hemicycle_questions_orales": 0,
                "hemicycle_questions_ecrites": 0,
                "commission_presences": 0,
                "commission_interventions": 0,
                "rapports": 0,
                "propositions_ecrites": 0,
                "propositions_signees": 0,
                "amendements": 0,
                "moyenne_presence_commission": 0,
                "moyenne_presence_assemblee": 0,
            },
            'ni': {
                "nb_gens": 0,
                "hemicycle_presence": 0,
                "hemicycle_interventions": 0,
                "hemicycle_questions_orales": 0,
                "hemicycle_questions_ecrites": 0,
                "commission_presences": 0,
                "commission_interventions": 0,
                "rapports": 0,
                "propositions_ecrites": 0,
                "propositions_signees": 0,
                "amendements": 0,
                "moyenne_presence_commission": 0,
                "moyenne_presence_assemblee": 0,
            },

        }

        for parti in differents_partis["groupe_politique"]:
            for depute in deputes:
                if depute['depute']['groupe_sigle'] == parti["name"]:
                    keyword = parti["keyword"]
                    dataPartiPolitique[keyword]["nb_gens"] += 1
                    dataPartiPolitique[keyword]["hemicycle_presence"] += (
                            depute['depute']['hemicycle_interventions'] + depute['depute'][
                        'hemicycle_interventions_courtes'])
                    dataPartiPolitique[keyword]["hemicycle_interventions"] += depute['depute'][
                        'hemicycle_interventions']
                    dataPartiPolitique[keyword]["hemicycle_questions_orales"] += depute['depute']['questions_orales']
                    dataPartiPolitique[keyword]["hemicycle_questions_ecrites"] += depute['depute']['questions_ecrites']
                    dataPartiPolitique[keyword]["commission_presences"] += depute['depute']['commission_presences']
                    dataPartiPolitique[keyword]["commission_interventions"] += depute['depute'][
                        'commission_interventions']
                    dataPartiPolitique[keyword]["rapports"] += depute['depute']['rapports']
                    dataPartiPolitique[keyword]["propositions_ecrites"] += depute['depute']['propositions_ecrites']
                    dataPartiPolitique[keyword]["propositions_signees"] += depute['depute']['propositions_signees']
                    dataPartiPolitique[keyword]["amendements"] += (
                            depute['depute']['amendements_proposes'] + depute['depute']['amendements_signes'] +
                            depute['depute']['amendements_adoptes'])

        for parti in differents_partis["groupe_politique"]:
            keyword = parti["keyword"]
            dataPartiPolitique[keyword]["moyenne_presence_commission"] = dataPartiPolitique[keyword][
                                                                             "commission_presences"] / \
                                                                         dataPartiPolitique[keyword]["nb_gens"]
            dataPartiPolitique[keyword]["moyenne_presence_assemblee"] = dataPartiPolitique[keyword][
                                                                            "hemicycle_presence"] / \
                                                                        dataPartiPolitique[keyword]["nb_gens"]

        df = pd.DataFrame(dataPartiPolitique).T.reset_index()

        img = io.BytesIO()

        plt.figure(figsize=(15, 10))
        sns.catplot(x='index', y='moyenne_presence_commission', kind='bar', data=df)
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)

        plot_url = base64.b64encode(img.getvalue()).decode('utf8')

        plt.figure(figsize=(15, 10))
        sns.catplot(x='index', y='moyenne_presence_assemblee', kind='bar', data=df)
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)

        moyenne_presence_assemblee = base64.b64encode(img.getvalue()).decode('utf8')

        return render_template('pages/groupe_politique.html', dataPartiPolitique=dataPartiPolitique,
                               differents_partis=differents_partis, plot_url=plot_url,
                               moyenne_presence_assemblee=moyenne_presence_assemblee)

    return app

app = create_app()


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
