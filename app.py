from flask import Flask, render_template
import requests
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import io 
import base64

app = Flask(__name__)

@app.route("/")
def home():
	response = requests.get('https://www.nosdeputes.fr/synthese/data/json')
	deputes = response.json()["deputes"]
	return render_template('pages/home.html', deputes=deputes)


@app.route("/selected/<int:id>/<prenom>/<nom>")
def depute_selected(id, nom, prenom):
	nom_complet = nom.lower() + '-'  + prenom.lower() 
	response = requests.get('https://www.nosdeputes.fr/synthese/data/json')
	deputes = response.json()["deputes"]

	presence_depute_mois = {
    "novembre_2021" : {},
    "decembre_2021" : {},
    "janvier_2021" : {},
    "fevrier_2021" : {}
	}

	presence_depute_mois["novembre_2021"] = requests.get('https://www.nosdeputes.fr/synthese/202111/json')
	presence_depute_mois["novembre_2021"] = presence_depute_mois["novembre_2021"].json()["deputes"][1-id]['depute']['commission_presences']
	presence_depute_mois["decembre_2021"] = requests.get('https://www.nosdeputes.fr/synthese/202112/json')
	presence_depute_mois["decembre_2021"] = presence_depute_mois["decembre_2021"].json()["deputes"][1-id]['depute']['commission_presences']
	presence_depute_mois["janvier_2021"] = requests.get('https://www.nosdeputes.fr/synthese/202001/json')
	presence_depute_mois["janvier_2021"] = presence_depute_mois["janvier_2021"].json()["deputes"][1-id]['depute']['commission_presences']
	presence_depute_mois["fevrier_2021"] = requests.get('https://www.nosdeputes.fr/synthese/202002/json')
	presence_depute_mois["fevrier_2021"] = presence_depute_mois["fevrier_2021"].json()["deputes"][1-id]['depute']['commission_presences']


	df_mois = pd.DataFrame(presence_depute_mois, index=[0]).T

	img = io.BytesIO()
	
	sns.relplot(data=df_mois, kind="line")
	plt.yticks([0,1,2,3,4,5, 6, 7, 8, 9, 10])
	plt.savefig(img, format='png')
	plt.close()
	img.seek(0)

	plot_url = base64.b64encode(img.getvalue()).decode('utf8')


	image = 'https://www.nosdeputes.fr/depute/photo/'+nom_complet+'/100'

	return render_template('pages/depute_selected.html', deputes=deputes,  depute_selected = id, image=image, plot_url=plot_url)


@app.route("/groupe-politique")
def groupe_politique():
	response = requests.get('https://www.nosdeputes.fr/synthese/data/json')
	deputes = response.json()["deputes"]

	differents_partis = {
    	"groupe_politique" : [
        	{"name" : "LREM", "keyword" : "lrem"},
        	{"name" : "LR", "keyword" : "lr"},
        	{"name" : "LFI", "keyword" : "lfi"},
        	{"name" : "GDR", "keyword" : "gdr"},
        	{"name" : "SOC", "keyword" : "soc"},
        	{"name" : "LT", "keyword" : "lt"},
        	{"name" : "MODEM", "keyword" : "modem"},
        	{"name" : "AE", "keyword" : "ae"},
        	{"name" : "UDI", "keyword" : "udi"},
        	{"name" : "NI", "keyword" : "ni"},
    	]

	}

	dataPartiPolitique = {	
    	'lr' : {
        	"hemicycle_presence" : 0,
			"hemicycle_interventions" : 0,
			"hemicycle_questions_orales" : 0,
			"hemicycle_questions_ecrites" : 0,
			"commission_presences" : 0,
			"commission_interventions" : 0,
			"rapports" : 0,
			"propositions_ecrites" : 0,
			"propositions_signees" : 0,
			"amendements" : 0,
    	},
    	'lrem' : {
        	"hemicycle_presence" : 0,
			"hemicycle_interventions" : 0,
			"hemicycle_questions_orales" : 0,
			"hemicycle_questions_ecrites" : 0,
			"commission_presences" : 0,
			"commission_interventions" : 0,
			"rapports" : 0,
			"propositions_ecrites" : 0,
			"propositions_signees" : 0,
			"amendements" : 0,
    	},
    	'lfi' : {
        	"hemicycle_presence" : 0,
			"hemicycle_interventions" : 0,
			"hemicycle_questions_orales" : 0,
			"hemicycle_questions_ecrites" : 0,
			"commission_presences" : 0,
			"commission_interventions" : 0,
			"rapports" : 0,
			"propositions_ecrites" : 0,
			"propositions_signees" : 0,
			"amendements" : 0,
    	},
    	'gdr' : {
        	"hemicycle_presence" : 0,
			"hemicycle_interventions" : 0,
			"hemicycle_questions_orales" : 0,
			"hemicycle_questions_ecrites" : 0,
			"commission_presences" : 0,
			"commission_interventions" : 0,
			"rapports" : 0,
			"propositions_ecrites" : 0,
			"propositions_signees" : 0,
			"amendements" : 0,
    	},
    	'soc' : {
        	"hemicycle_presence" : 0,
			"hemicycle_interventions" : 0,
			"hemicycle_questions_orales" : 0,
			"hemicycle_questions_ecrites" : 0,
			"commission_presences" : 0,
			"commission_interventions" : 0,
			"rapports" : 0,
			"propositions_ecrites" : 0,
			"propositions_signees" : 0,
			"amendements" : 0,
    	},
    	'lt' : {
        	"hemicycle_presence" : 0,
			"hemicycle_interventions" : 0,
			"hemicycle_questions_orales" : 0,
			"hemicycle_questions_ecrites" : 0,
			"commission_presences" : 0,
			"commission_interventions" : 0,
			"rapports" : 0,
			"propositions_ecrites" : 0,
			"propositions_signees" : 0,
			"amendements" : 0,
    	},
    	'modem' : {
        	"hemicycle_presence" : 0,
			"hemicycle_interventions" : 0,
			"hemicycle_questions_orales" : 0,
			"hemicycle_questions_ecrites" : 0,
			"commission_presences" : 0,
			"commission_interventions" : 0,
			"rapports" : 0,
			"propositions_ecrites" : 0,
			"propositions_signees" : 0,
			"amendements" : 0,
    	},
    	'ae' : {
        	"hemicycle_presence" : 0,
			"hemicycle_interventions" : 0,
			"hemicycle_questions_orales" : 0,
			"hemicycle_questions_ecrites" : 0,
			"commission_presences" : 0,
			"commission_interventions" : 0,
			"rapports" : 0,
			"propositions_ecrites" : 0,
			"propositions_signees" : 0,
			"amendements" : 0,
    	},
    	'udi' : {
        	"hemicycle_presence" : 0,
			"hemicycle_interventions" : 0,
			"hemicycle_questions_orales" : 0,
			"hemicycle_questions_ecrites" : 0,
			"commission_presences" : 0,
			"commission_interventions" : 0,
			"rapports" : 0,
			"propositions_ecrites" : 0,
			"propositions_signees" : 0,
			"amendements" : 0,
    	},
    	'ni' : {
        	"hemicycle_presence" : 0,
			"hemicycle_interventions" : 0,
			"hemicycle_questions_orales" : 0,
			"hemicycle_questions_ecrites" : 0,
			"commission_presences" : 0,
			"commission_interventions" : 0,
			"rapports" : 0,
			"propositions_ecrites" : 0,
			"propositions_signees" : 0,
			"amendements" : 0,
    	},
		
	}





	for parti in differents_partis["groupe_politique"]:
		for depute in deputes : 
			if depute['depute']['groupe_sigle'] == parti["name"] :
				keyword = parti["keyword"]
				dataPartiPolitique[keyword]["hemicycle_presence"] += (depute['depute']['hemicycle_interventions'] + depute['depute']['hemicycle_interventions_courtes'])
				dataPartiPolitique[keyword]["hemicycle_interventions"] += depute['depute']['hemicycle_interventions']
				dataPartiPolitique[keyword]["hemicycle_questions_orales"] += depute['depute']['questions_orales']
				dataPartiPolitique[keyword]["hemicycle_questions_ecrites"] += depute['depute']['questions_ecrites']
				dataPartiPolitique[keyword]["commission_presences"] += depute['depute']['commission_presences']
				dataPartiPolitique[keyword]["commission_interventions"] += depute['depute']['commission_interventions']
				dataPartiPolitique[keyword]["rapports"] += depute['depute']['rapports']
				dataPartiPolitique[keyword]["propositions_ecrites"] += depute['depute']['propositions_ecrites']
				dataPartiPolitique[keyword]["propositions_signees"] += depute['depute']['propositions_signees']
				dataPartiPolitique[keyword]["amendements"] += (depute['depute']['amendements_proposes'] + depute['depute']['amendements_signes'] + depute['depute']['amendements_adoptes'])

	df = pd.DataFrame(dataPartiPolitique).T.reset_index()
	
	img = io.BytesIO()
	
	plt.figure(figsize=(15,10))
	sns.catplot(x= 'index', y='hemicycle_presence', kind= 'bar', data = df)
	plt.savefig(img, format='png')
	plt.close()
	img.seek(0)

	plot_url = base64.b64encode(img.getvalue()).decode('utf8')


	return render_template('pages/groupe_politique.html',  dataPartiPolitique = dataPartiPolitique, differents_partis = differents_partis, plot_url=plot_url)

if __name__ == '__main__' :
	app.run(debug=True)
