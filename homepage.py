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
st.title("Welcome to my website! 😎") # Page title


# Blurb about me
"""
:wave: My name is Mark Stansky, a finance analyst turned python programmer and data scientist via Brainstation NYC's intensive 12 week DS Bootcamp.
"""
"""
:chart: I created this website to showcase my capstone project, an interactive machine learning model that predicts the (%) likelihood 
of S&P 500 Stocks going bankrupt within the next year.
It also turned out to be a great way to learn and practice AWS and containerizing applications in Docker.
To understand what went into the model's creation, I suggest you start by reading Behind the Bankruptcy Project, available in the sidebar.

    You can find the writeup and interactive demo in the sidebar.


:radio: Stay tuned and check back soon, I in addition to a bankruptcy 2.0 model I plan to finish and post some other projects I have in the works.  
If you have feedback about my project or anything else relating to my work, please also feel free to reach out and contact me at any of my social links below.  I am am all ears.
"""

st.image('./media/bstn_demo_day_1.jpeg', caption= 'Here\'s me at demo day')

# Roadmap
st.markdown("""
# Updates
- Bankruptcy v1.0 writeup added (Feb '24)
- Application containerized in Docker and Deployed on AWS (Dec '23)

# Roadmap 🏍️💨
- Expand Bankruptcy Analysis from S&P 500 to Russell 3,000
- Incorporate explainability -- WHY is this company likely to go bankrupt?  What features made you decide this?
- Incorporate Macroeconomic data -- bankruptcies happen in certain environments, can we identify them and correspondingly vulnerable companies?

""")
st.code('Last updated Feb 6, 2024')



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