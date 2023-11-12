import database as db
import pymongo
import streamlit as st
from pandas import DataFrame
import time

st.title('Hug Bounter v2 🕷️')

st.write("Be the first to report the bug!")


selected = st.selectbox("Platforms:", ("YesWeHack","Intigriti","Bugcrowd","HackerOne"), index=None, placeholder="Select a platform")


if selected == 'YesWeHack':
	data = db.read_collection('YesWeHack')
	st.write(len(data), " records available")

elif selected == 'Intigriti':
	data = db.read_collection('Intigriti')
	st.write(len(data), " records available")

elif selected == 'Bugcrowd':
	data = db.read_collection('Bugcrowd')
	st.write(len(data), " records available")

elif selected == 'HackerOne':
	data = db.read_collection('HackerOne')
	st.write(len(data), " records available")

button = st.button("Show records")


if selected =='YesWeHack' and button:

	with st.status("Loading...", expanded=True) as status:
	    st.write("Connecting to server...")
	    time.sleep(2)
	    st.write("Fetching data...")
	    time.sleep(1)
	    st.write("Creating data frame...")
	    time.sleep(1)
	    status.update(label="All records fetched!", state="complete", expanded=False)

	st.write(data)
	# -- 'data' (DataFrame) is not a supported download format -- #
	# -- convert_df func called to turn 'data' into csv format -- #
	csv = db.convert_df(data)
	st.download_button(
	label="Download csv 📄",
	data=csv,
	file_name="YesWeHack-Public-Programs",
	mime="text/csv",
	)



elif selected =='Intigriti' and button:

	with st.status("Loading...", expanded=True) as status:
	    st.write("Connecting to server...")
	    time.sleep(2)
	    st.write("Fetching data...")
	    time.sleep(1)
	    st.write("Creating data frame...")
	    time.sleep(1)
	    status.update(label="All records fetched!", state="complete", expanded=False)

	st.write(data)
	csv = db.convert_df(data)
	st.download_button(
	label="Download csv 📄",
	data=csv,
	file_name="Intigriti-Public-Programs",
	mime="text/csv",
	)

elif selected =='Bugcrowd' and button:

	with st.status("Loading...", expanded=True) as status:
	    st.write("Connecting to server...")
	    time.sleep(2)
	    st.write("Fetching data...")
	    time.sleep(1)
	    st.write("Creating data frame...")
	    time.sleep(1)
	    status.update(label="All records fetched!", state="complete", expanded=False)

	st.write(data)
	csv = db.convert_df(data)
	st.download_button(
	label="Download csv 📄",
	data=csv,
	file_name="Bugcrowd-Public-Programs",
	mime="text/csv",
	)

elif selected =='HackerOne' and button:

	with st.status("Loading...", expanded=True) as status:
	    st.write("Connecting to server...")
	    time.sleep(2)
	    st.write("Fetching data...")
	    time.sleep(1)
	    st.write("Creating data frame...")
	    time.sleep(1)
	    status.update(label="All records fetched!", state="complete", expanded=False)

	st.write(data)
	csv = db.convert_df(data)
	st.download_button(
	label="Download csv 📄",
	data=csv,
	file_name="HackerOne-Public-Programs",
	mime="text/csv",
	)


st.divider()

operation = st.radio(
    "Choose operation:",
    ["Update", "Insert", "Drop"],
    captions = ["Update database from source for latest scopes & programs", "Update database manually by entering new record(s)", "Manually drop program(s)"], index=None)

if operation == 'Insert':
	with st.expander("Enter program details"):
		with st.form("insert_form"):
			platform = st.selectbox("Platform:", ("YesWeHack", "Intigriti", "Bugcrowd", "HackerOne"), index=None, placeholder="Please select a platform")
			title = st.text_input("Program name:")
			description = st.text_input("Description:")
			scope = st.text_input("Scope:")
			submitted = st.form_submit_button("Submit")

			if submitted:
				if platform == None or title == '' or description == '' or scope == '':
					toast = st.toast('All fields are required!')
					#time.sleep(5)
					#toast.empty()
				else:
					db.manual_update(platform, title, description, scope)
					st.success("Record successfully added!")
					st.cache_data.clear()

if operation == 'Drop':
	with st.form("Delete form"):
		selected = st.selectbox("Platform:", ("YesWeHack", "Intigriti", "Bugcrowd", "HackerOne"), index=None, placeholder="Please select a platform")
		title = st.text_input("Program name:")
		submitted = st.form_submit_button("Delete")
		if selected and submitted: 
			#st.info(db.delete_record(selected, title))
			db.delete_record(selected, title)
			#st.warning(str(title) + " removed!")
			st.cache_data.clear()
		elif not selected and submitted:
			toast = st.toast('Please select a platform!')
			#time.sleep(5)
			#toast.empty()

if operation == 'Update':
	with st.form("Update"):
		selected_to_update = st.selectbox("Platforms:", ("YesWeHack", "Intigriti", "Bugcrowd", "HackerOne"), index=None, placeholder="Please select a platform")
		submitted = st.form_submit_button("Update")
		if selected_to_update and submitted:
			db.update_collection(selected_to_update)
			st.success(selected_to_update + " database successfully updated!")
			st.cache_data.clear()
		elif not selected_to_update and submitted:
			toast = st.toast('Please select a platform!')
			#time.sleep(5)
			#toast.empty()
