import streamlit as st
import pandas
import plotly.express as px
import numpy

st.set_page_config("Learning Streamlit")
st.header("Welcome to Learning Streamlit")
st.subheader("Streamlit Components")
st.markdown("Turn your data scripts into shareable web apps in minutes.All in pure Python. No front‑end experience required.")
st.markdown("_Turn your data scripts into shareable web apps in minutes.All in pure Python. No front‑end experience required._")
st.latex("y = mx+c")
st.text("This is my first text.")
st.caption("This is my second.")
st.code(""" 
        def print_statement():
            print("Hello World)
        print_statement()
""", language="python")

st.subheader("Data Display Elements")
data = pandas.read_csv('/Users/amru/Volume/Learning/Gen AI/products.csv')
st.dataframe(data)
# st.table(data)
json_data = {
    'a' : {
        "Name" : "Nani",
        "Age" : 32,
        "Occupation" : "Actor"
    },
    'b' : {
        "Name" : "Jai",
        "Age" : 32,
        "Occupation" : "Doctor"
    }
}
st.json(json_data)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric('Apple', '$72', '45')
with col2:
    st.metric('GoldBees', '$456', '-12')
with col3:
    st.metric('IndusBank', '$502', '-09')

st.subheader("Input Widgets")
submit = st.checkbox("Show Data")
if submit:
    st.dataframe(data)
st.radio("Choose one", ('a', 'b', 'c'))
selected_value = st.selectbox('Select the option', data.columns)
st.write(f"The selected value is _{selected_value}_")

a = st.slider("Select a value : ", 0,100,0)
b = st.slider("Select b value : ",0.0,5.0,1.5)
c = a+b
st.write(f"Sum of Slider value is {c}")

multi_values = st.multiselect("Seelct the options", data.columns)
st.write(f"The selected multi value are _{multi_values}_")

st.subheader("Media widgets")
check_img = st.checkbox("Show Image")
if check_img:
    st.image('/Users/amru/Downloads/image1.png')

play_video = st.checkbox("Play Video")
if play_video:
    vid = open('/Users/amru/Volume/Learning/Gen AI/153478-805374138_medium.mp4', 'rb')
    st.video(vid, format='video/mp4')

play_audio = st.checkbox("Play Audio")
if play_audio:
    audio = open('/Users/amru/Volume/Learning/Gen AI/guitar_music.mp3', 'rb')
    st.audio(audio, format='video/mp3')

st.subheader("Plotly charts in Streamlit")
columns = list(data.columns)
target = st.selectbox("Choose the target:", columns)
col2 = columns.copy()
col2.remove(target)
x_var = st.selectbox("Choose the X variable:", col2)
y_var = st.selectbox("Choose the Y variable:", col2)
fig = px.scatter(data, x=x_var, y=y_var,color=target)
st.plotly_chart(fig)

st.subheader("Line Chart")
data_df = pandas.DataFrame(numpy.random.rand(20,3), columns=['a', 'b', 'c'])
st.line_chart(data_df, width='stretch')
st.subheader("Bar Chart")
st.bar_chart(data_df)
st.subheader("Area Chart")
st.area_chart(data_df)

st.subheader("Status Elements")

st.success("This is success function.")
st.info("This is info function.")
st.warning("This is warning function.")
st.error("This is error function.")

def divisible():
    try:
        a = 10/0
    except Exception as e:
        st.exception(e)

divisible()

st.subheader("Download Button")

def data_dload(data):
    return data.to_csv().encode('utf-8')

data_dload(data)
st.download_button(
    label='Download CSV File',
    data='csv',
    file_name='Download-Product.csv',
    mime='text/csv'
)

with open('/Users/amru/Downloads/nani_image.jpg', 'rb') as file:
    file_bytes = file.read()
st.download_button(
    label='Download Image',
    data = file_bytes,
    file_name='nani_image.jpg',
    mime='image/jpeg'
)

st.subheader("Streamlit app with SQLite3")