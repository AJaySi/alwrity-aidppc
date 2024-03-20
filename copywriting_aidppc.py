import time
import os
import json
import openai
import streamlit as st
from streamlit_lottie import st_lottie
from tenacity import retry, stop_after_attempt, wait_random_exponential

def main():
    set_page_config()
    custom_css()
    hide_elements()
    sidebar()
    title_and_description()
    input_section()

def set_page_config():
    st.set_page_config(
        page_title="Alwrity",
        layout="wide",
        page_icon="img/logo.png"
    )

def custom_css():
    st.markdown("""
        <style>
            .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
                padding-left: 1rem;
                padding-right: 1rem;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
            [class="st-emotion-cache-7ym5gk ef3psqc12"] {
                display: inline-block;
                padding: 5px 20px;
                background-color: #4681f4;
                color: #FBFFFF;
                width: 300px;
                height: 35px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                border-radius: 8px;
            }
        </style>
    """, unsafe_allow_html=True)

def hide_elements():
    hide_decoration_bar_style = '<style>header {visibility: hidden;}</style>'
    st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

    hide_streamlit_footer = '<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>'
    st.markdown(hide_streamlit_footer, unsafe_allow_html=True)

def sidebar():
    st.sidebar.title("Attention-Interest-Description-Persuasion-Proof-Close")
    st.sidebar.image("img/alwrity.jpeg", use_column_width=True)
    st.sidebar.markdown("🧕 :red[Checkout Alwrity], complete **AI writer & Blogging solution**:[Alwrity](https://alwrity.netlify.app)")


def title_and_description():
    st.title("✍️ Alwrity - AI Generator for CopyWriting AIDPPC Formula")
    with st.expander("What is **Copywriting AIDPPC formula** & **How to Use**? 📝❗"):
        st.markdown('''
            ### What's AIDPPC copywriting Formula, and How to use this AI generator 🗣️
            ---
            #### AIDPPC Copywriting Formula

            AIDPPC stands for Attention-Interest-Description-Persuasion-Proof-Close. It's a comprehensive copywriting formula that involves:

            1. **Attention**: Grabbing the audience's attention with a compelling headline or opening statement.
            2. **Interest**: Generating interest by highlighting the benefits or solving a problem for the audience.
            3. **Description**: Describing the product or service in detail, emphasizing its features and unique selling points.
            4. **Persuasion**: Persuading the audience to take action by presenting compelling arguments or incentives.
            5. **Proof**: Providing social proof or evidence to support the claims made in the copy.
            6. **Close**: Prompting the audience to take the final step, such as making a purchase or signing up.

            The AIDPPC formula guides copywriters in creating persuasive and convincing content that leads the audience to action.

            #### AIDPPC Copywriting Formula: Simple Example

            - **Attention**: Catchy headline: "Discover the Secret to Boosting Your Productivity!"
            - **Interest**: Highlighting benefits: "Our productivity tool helps you save time and stay organized."
            - **Description**: Features overview: "With built-in task lists, calendar integration, and collaboration tools."
            - **Persuasion**: Call to action: "Start your free trial today and experience the difference!"
            - **Proof**: Testimonials or reviews: "Rated 5 stars by thousands of satisfied users."
            - **Close**: Urgency or incentive: "Limited time offer - get 20% off when you sign up now!"

            ---
        ''')


def input_section():
    with st.expander("**PRO-TIP** - Easy Steps to Create Compelling Copy", expanded=True):
        col1, space, col2 = st.columns([5, 0.1, 5])
        with col1:
            brand_name = st.text_input('**Enter Brand/Company Name**', help="Enter the name of your brand or company.")
        with col2:
            description = st.text_input('**Describe What Your Company Does ?** (In 2-3 words)', help="Describe your product or service briefly.")
        col1, space, col2 = st.columns([5, 0.1, 5])
        with col1:
            interest = st.text_input('**Generate Interest** (Describe your Services)', 
                         help="For example: 'Solve a problem for your audience, such as providing convenience or saving time.'",
                         placeholder="Save time, convenience, affordable, better service, in minutes, safety...")
        with col2:
            close = st.text_input('**Prompt Action** (Call To Action-CTA)', 
                      help="Guide: 'Encourage the audience to take the final step, like making a purchase or signing up.'",
                      placeholder="Buy/Book/Try now, Sign up, Try for free, Early bird offers, Sale...")

        if st.button('**Get AIDPPC Copy**'):
            if  interest.strip() and close.strip():
                with st.spinner("Generating AIDPPC Copy..."):
                    aidppc_copy = generate_aidppc_copy(brand_name, description, interest, close)
                    if aidppc_copy:
                        st.subheader('**👩🔬👩🔬 Your AIDPPC Copy**')
                        st.markdown(aidppc_copy)
                    else:
                        st.error("💥 **Failed to generate AIDPPC copy. Please try again!**")
            else:
                st.error("All fields are required!")

    page_bottom()


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def generate_aidppc_copy(brand_name, description, interest, close):
    prompt = f"""As an expert copywriter, I need your help in creating a marketing campaign for {brand_name},
        which is a {description}. Your task is to use the AIDPPC (Attention-Interest-Description-Persuasion-Proof-Close) formula to craft compelling copy. Present Compelling Arguments or Incentives to Persuade. Solve a Problem to Generate Interest for {interest}. Prompt the Audience to Take the Final Step for {close}.
    """
    return openai_chatgpt(prompt)


def page_bottom():
    """ """
    data_oracle = import_json(r"lottie_files/brain_robot.json")
    st_lottie(data_oracle, width=600, key="oracle")

    st.markdown('''
    Copywrite using AIDPPC formula - powered by AI (OpenAI, Gemini Pro).

    Implemented by [Alwrity](https://alwrity.netlify.app).

    Learn more about [Google's Stance on AI generated content](https://alwrity.netlify.app/post/googles-guidelines-on-using-ai-generated-content-everything-you-need-to-know).
    ''')

    st.markdown("""
    ### Attention:
    Are you tired of struggling to create effective marketing campaigns that engage your audience?

    ### Interest:
    Imagine having access to a powerful tool that crafts compelling copy effortlessly, saving you time and effort.

    ### Description:
    Introducing Alwrity - Your AI Generator for Copywriting AIDPPC Formula. With Alwrity, you can create persuasive marketing campaigns that drive action effectively.

    ### Persuasion:
    Don't let ineffective copywriting hold back your business. Try Alwrity today and revolutionize your marketing efforts!

    ### Proof:
    Trusted by thousands of users, Alwrity has helped businesses like yours achieve their marketing goals.

    ### Close:
    Start creating persuasive copy with Alwrity now and see the difference it makes in your marketing campaigns!
    """)



@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def openai_chatgpt(prompt, model="gpt-3.5-turbo-0125", max_tokens=500, top_p=0.9, n=1):
    try:
        client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            n=n,
            top_p=top_p
        )
        return response.choices[0].message.content
    except openai.APIError as e:
        st.error(f"OpenAI API Error: {e}")
    except openai.APIConnectionError as e:
        st.error(f"Failed to connect to OpenAI API: {e}")
    except openai.RateLimitError as e:
        st.error(f"Rate limit exceeded on OpenAI API request: {e}")
    except Exception as err:
        st.error(f"An error occurred: {err}")


# Function to import JSON data
def import_json(path):
    with open(path, "r", encoding="utf8", errors="ignore") as file:
        url = json.load(file)
        return url



if __name__ == "__main__":
    main()

