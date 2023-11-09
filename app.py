import requests
import streamlit as st
import database as db

st.title("Hug Bounter")

st.subheader("Integrated with deta space")

st.write("Hug Bounter now stores/reads data in a NoSQL database (deta.space) for better optimization and accessibility.")
st.write("Happy hunting ;-)")

url = "https://raw.githubusercontent.com/Osb0rn3/bugbounty-targets/main/programs/yeswehack.json"
r = requests.get(url)
data = r.json()

#data_list = []


platform = st.selectbox("Select a Platform", ( "Hacker1", "Intigriti", "BugCrowd", "YesWeHack"))

action = st.selectbox("Select Action", ("Retrieve Database", "Update Database"))

button = st.button("Submit")

if button:
	if platform == "YesWeHack" and action == "Update Database":
		db.update_yeswehack()
		st.success("YesWeHack database updated successfully!")

	elif platform == "YesWeHack" and action == "Retrieve Database":
		db.retrieve_yeswehack()
		st.success("YesWeHack database retrieved successfully!")
		st.write(db.retrieve_yeswehack())

	elif platform == "Hacker1" and action == "Update Database":
		# TODO: Update Hacker1
		st.success("Updated Hacker1")

	elif platform == "Hacker1" and action == "Retrieve Database":
		# TODO: Retrieve Hacker1
		st.success("Hacker1 DB Retrieved")

	elif platform == "BugCrowd" and action == "Update Database":
		db.update_bugcrowd()
		st.success("Updated BugCrowd")
		st.write(db.update_bugcrowd())

	elif platform == "BugCrowd" and action == "Retrieve Database":
		db.retrieve_bugcrowd()
		st.success("Bugcrowd database retrieved successfully!")
		st.write(db.retrieve_bugcrowd())

	elif platform == "Intigriti" and action == "Update Database":
		db.update_intigriti()
		st.success("Intigriti database updated successfully!")

	elif platform == "Intigriti" and action == "Retrieve Database":
		db.retrieve_intigriti()
		st.success("Intigriti database retrieved successfully!")
		st.write(db.retrieve_intigriti())


del_all = st.button("Delete all records")
if del_all:
	db.delete_all_records()
	st.write("All records were erased.")