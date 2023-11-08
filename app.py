import requests
import streamlit as st


#------------BACKGROUND IMAGE------------#
page_bg_img = '''
<style>
.stApp {
background-image: url("https://png2.cleanpng.com/sh/c9d2fe633c9376473afe0d7ae95613a2/L0KzQYm3VcI4N5h2kJH0aYP2gLBuTflve5ZojJ9rZXSwcsbuTgNwbqV8eeRuLXL4d37qjB1xfaVqip9yY3Bxg37qjPlxNZJ3RadrMHHoRbSCUcNlO2U6RqU5OUC6SYWCUcUzP2U5SKo9MUC7QYO1kP5o/kisspng-insect-bed-bug-software-bug-computer-icons-clip-ar-5b0ae5c913d345.3090794915274408410812.png");
background-size: contain;
background-repeat: no-repeat;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)


#------------HIDE STREAMLIT STYLE------------#
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)


st.title("Hug Bounty")

home_text = """
Use Hug Bounty to get the latest additions to the most popular bug bounty platforms and their programs. Simply select your prefered platform and enjoy the results. Currently supporting only the last 20 added programs.\n \n Happy hunting ;-)"""

st.sidebar.header("Sidebar")

option = st.sidebar.selectbox("Platforms: ", ("Please select a platform" ,"Hacker1", "Bugcrowd", "Intigrity", "YesWeHack"))


def remove_html_tags(text):
	"""REMOVE HTML TAGS FROM A STRING"""
	import re
	clean = re.compile('<.*?>')
	return re.sub(clean, '', text)


#------------HACKERONE OPTION------------#
if option == 'Hacker1':
	home_text = ''
	st.header(option + " Programs:")
	r = requests.get("https://raw.githubusercontent.com/Osb0rn3/bugbounty-targets/main/programs/hackerone.json")
	data = r.json()

	count = 1 

	for i in data[:20]:

		col1, col2 = st.columns([1,1])

		with col1:
			try:
				st.image(i["attributes"]["profile_picture"])
			except:
				pass
			try:
				st.write("Submission: ", i["attributes"]["submission_state"])
			except:
				pass
			try:
				st.write("Start Date: ", i["attributes"]["started_accepting_at"])
			except:
				pass
			try:
				st.write("State: ", i["attributes"]["submission_state"])
			except:
				pass
			
		with col2:
			st.write(count)
			count+=1
			try:
				st.write("Title: ", i["attributes"]["name"])
			except:
				pass
			try:
				st.write("Bounty: ", i["attributes"]["offers_bounties"])
			except:
				pass
			try:
				st.write("Currency: ", i["attributes"]["currency"])
			except:
				pass
			try:
				st.write("Active Triage: ", i["attributes"]["triage_active"])
			except:
				pass
		
		with st.expander("View Scope"):
			scope = i["relationships"]["structured_scopes"]["data"]
			for i in scope:
				st.write(i["attributes"])
				
			

		st.divider()


#------------BUGCROWD OPTION------------#	
if option == 'Bugcrowd':
	home_text = ''
	st.header(option + " Programs:")

	r = requests.get("https://raw.githubusercontent.com/Osb0rn3/bugbounty-targets/main/programs/bugcrowd.json")
	data = r.json()

	count = 1

	for i in data[:20]:
		
		col1, col2 = st.columns([1,1])
		with col1:
			st.image(i["logo"])
		
		with col2:


			st.write(count)
			count+=1

			try:	
				st.write("Title: ", i["name"])
			except:
				pass
			try:		
				st.write("Type: ", i["participation"])
			except:
				pass
			try:	
				st.write("Program URL: ", "https://bugcrowd.com"+i["program_url"])	
			except:
				pass	
			try:
				st.write("Industry: ", i["industry_name"])
			except:
				pass
			try:	
				st.write("Minimum Bounty: ", i["min_rewards"])
			except:
				pass
			try:
				st.write("Maximum Bounty: ", i["max_rewards"])		
			except:
				pass

		try:
			st.info(i["tagline"])
		except:
			pass


		desc = i["target_groups"][0]["description_html"]
		
		with st.expander("Additional Info"):
			st.markdown(desc, unsafe_allow_html=True)
			if desc == '':
				st.error("No additional info found!")


		with st.expander("View Scope"):
			st.write(i["target_groups"])
		
		st.divider()


#------------INTIGRITI OPTION------------#
if option == 'Intigrity':
	home_text = ''
	st.header(option + " Programs:")
	r = requests.get("https://raw.githubusercontent.com/Osb0rn3/bugbounty-targets/main/programs/intigriti.json")
	data = r.json()

	count = 1

	for i in data[:20]:

		col1, col2 = st.columns([1,1])

		with col1:
			try:
				logo = "https://bff-public.intigriti.com/file/" + i["logoId"]
				st.image(logo)
			except:
				pass
		
		with col2:
			st.write(count)
			count+=1
			try:
				st.write("Title: ", i["name"])
			except:
				pass
			try:		
				st.write("ID: ", i["programId"])
			except:
				pass
			try:	
				st.write("Confidentiality: ", i["confidentialityLevel"])
			except:
				pass

		try:
			st.info(i["description"])
		except:
			pass
		try:	
			st.write("Minimum Bounty: ", int(i["minBounty"]["value"]), i["minBounty"]["currency"])
		except:
			pass
		try:
			st.write("Maximum Bounty: ", int(i["maxBounty"]["value"]), i["maxBounty"]["currency"])
		except:
			pass

		with st.expander("View Scope"):
			st.write("Scope: ")
			st.write(i["domains"])

		st.divider()


#------------YESWEHACK OPTION------------#
if option == 'YesWeHack':
	home_text = ''
	st.header(option + " Programs:")
	r = requests.get("https://raw.githubusercontent.com/Osb0rn3/bugbounty-targets/main/programs/yeswehack.json")
	data = r.json()

	count = 1

	for i in data[:20]:
		col1, col2 = st.columns([1,1])		
		
		with col1:

			try:
				st.image(i["business_unit"]["logo"]["url"])
			except:
				pass

		with col2:

			st.write(count)
			count+=1
			try:
				st.write("Title: ", i['title'])
			except:
				pass
			try:	
				st.write("Public :", i['public'])
			except:
				pass
			try:
				st.write("Bounty: ",i['bounty'])
			except:
				pass
			try:
				has_bounty = i['bounty']
				if has_bounty is True:
					st.write("Minimum Bounty: ", i['bounty_reward_min'])
					st.write("Maximum Bounty: ", i['bounty_reward_max'])
			except:
				pass
			try:
				st.write("Reoports count: ",i['reports_count'])
			except:
				pass
			try:
				st.write("Scopes count :", i['scopes_count'])
			except:
				pass
		
		st.info(i['business_unit']['description'])
		st.write("Currency: ", i['business_unit']['currency'])

		with st.expander("View Scope"):
			st.write(i['scopes'])
		
		st.divider()

st.write(home_text)
