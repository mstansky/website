# Housekeeping
import streamlit as st

# Page Configuration --------------
st.set_page_config(
    page_title = "MrStansky",    # visible in tab on web browser
    page_icon = "✅",            # visible in tab on web browser
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None, # Should I add anything?
        'Report a bug': None, # Should I add an email me dialogue? or a Contact Me?
        'About': """# Thanks for visiting my website! 
Feel free to add me on one of my socials."""
    }
)
### Sidebar config -------------------------

st.sidebar.info("Select the homepage or a project above.") # Blue box on browser

### Page body config -----------------------
st.title("Welcome to Mr.Stansky 😎") # Page title

# Blurb about me
"""
My name is Mark Stansky, a finance analyst turned python programmer and data scientist via Brainstation NYC's intensive 12 week DS Bootcamp.

I created this blog to showcase my capstone project, a machine learning model attempting to predict the (%) likelihood 
of S&P 500 Stocks going bankrupt within the next year.

    You can find this project in the sidebar (v1.0).

Stay tuned, I will continue to improve upon the bankruptcy project in the upcoming weeks alongside some other project ideas I'm seeking to explore.
"""

# Roadmap
st.markdown("""
# Roadmap 🏍️💨
- Expand Company Data from S&P 500 to Russell 3,000
- Incorporate explainability -- WHY is this company likely to go bankrupt?
- Incorporate Macroeconomic data -- bankruptcies happen in certain environments, can we identify them and correspondingly vulnerable companies?

""")




# Session state check -> be able to use the session state from another page
# if "my_input" not in st.session_state:
#     st.session_state["my_input"] = ""
#
# my_input = st.text_input("Input a text here",st.session_state["my_input"])
# submit = st.button("Submit")
# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("You have entered: ", my_input)

# Add a logo / profile to the top: This is hacky and would need to be called on each page
def add_logo():
    st.markdown(
        """
        <div class="social-links">
            <a href="https://www.linkedin.com/in/markstansky/" target="_blank" class="linkedin-icon">LinkedIn</a>
            <a href="https://github.com/mstansky" target="_blank" class="github-icon">GitHub</a>
        </div>
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(http://placekitten.com/200/200); 
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "Mark's Blog";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        
          .social-links {
            display: flex;
            justify-content: space-between;
            margin: 10px 0;
          }
        
          .social-links a {
            text-decoration: none;
            color: #333;
            padding: 5px;
            border-radius: 5px;
            transition: background-color 0.3s ease;
          }
        
          .social-links a:hover {
            background-color: #eee;
          }
        
          .linkedin-icon::before {
            content: "\f08c"; /* LinkedIn Font Awesome icon code */
            font-family: "Font Awesome 5 Free";
            margin-right: 5px;
          }
        
          .github-icon::before {
            content: "\f09b"; /* GitHub Font Awesome icon code */
            font-family: "Font Awesome 5 Free";
            margin-right: 5px;
          }
        </style>
        """,
        unsafe_allow_html=True,
    )

# add_logo()

"#### Connect with me:"

st.markdown(
"""
    <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

    <div class="social-links">
      <a href="https://www.linkedin.com/in/markstansky/" target="_blank" class="linkedin-icon">LinkedIn</a>
      <a href="https://github.com/mstansky" target="_blank" class="github-icon">GitHub</a>
        </div>

    <style>
          .social-links {
            display: flex;
            justify-content: space-between;
            margin: 10px 0;
          }
    
          .social-links a {
            text-decoration: none;
            color: #333;
            padding: 5px;
            border-radius: 5px;
            transition: background-color 0.3s ease;
          }
    
          .social-links a:hover {
            background-color: #eee;
          }
    
          .linkedin-icon::before {
            content: "\f08c"; 
            font-family: "Font Awesome 5 Free";
            margin-right: 5px;
          }
    
          .github-icon::before {
            content: "\f09b"; 
            font-family: "Font Awesome 5 Free";
            margin-right: 5px;
          }
    </style>

    </head>
""",
    unsafe_allow_html=True,)