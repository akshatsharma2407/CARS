import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import json

df1 = pd.read_csv("CAR1.CSV")
df2 = pd.read_csv("CAR2.CSV")
df3 = pd.read_csv("CAR3.CSV")
df4 = pd.read_csv("CAR4.CSV")
df = pd.concat([df1,df2,df3,df4],axis=0)
df.dropna(inplace=True)
del df1,df2,df3,df4

# Set the page configuration as the very first command
st.set_page_config(
    page_title="Car Trends Dashboard",
    layout="wide",  # Use the full-width layout
    initial_sidebar_state="expanded",
)

def home():
# Flag for audio state
    if 'mute' not in st.session_state:
        st.session_state['mute'] = False  # Start with audio unmuted

    # Header
    st.title('🚗 Car Trends Dashboard')

    # Introduction
    st.write(
        """
        Welcome to the **Car Trends Dashboard**—an innovative platform designed to explore and analyze car trends globally. This tool offers a comprehensive overview of car brands, models, and market dynamics, empowering enthusiasts, analysts, and decision-makers to make informed choices in the automotive industry.
        """
    )

    # Create columns
    col1, col2, col3 = st.columns(3)

    # Content for the first column
    with col1:
        st.subheader('🗺️ Interactive Maps')
        st.write(
            """
            **Discover Geographical Insights**  
            Visualize car brand popularity and distribution across different regions. Identify emerging trends and hotspots with our interactive maps, offering a unique perspective on the automotive landscape.
            """
        )
        st.divider()

        st.subheader('📑 Custom Reports')
        st.write(
            """
            **Generate Tailored Insights**  
            Create custom reports based on specific criteria and filters. Whether you are interested in a particular brand, model, or market trend, generate reports that cater to your specific research needs.
            """
        )
        st.divider()

        st.subheader('📰 Blog and Insights')
        st.write(
            """
            **Stay Informed with Our Latest Articles**  
            Visit our blog for the latest articles on Python and DataScience.
            """
        )

    # Add vertical space between columns
    st.write("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    # Content for the second column
    with col2:
        st.subheader('📊 Model and Series Analysis')
        st.write(
            """
            **Understand Market Dynamics**  
            Analyze trends in car models and series using dynamic charts and graphs. Identify patterns in sales, preferences, and market fluctuations over time, allowing you to stay ahead in the automotive market.
            """
        )
        st.divider()

        st.subheader('🔍 Ownership and Origin Analysis')
        st.write(
            """
            **Gain Historical Perspectives**  
            Explore the historical evolution of car brands, ownership, and origins. Understand how brands have transformed over time and their impact on the automotive industry today.
            """
        )
        st.divider()

        st.subheader('ℹ️ About Me')
        st.write(
            """
            **Connect with me on Linkedin to make this kind of project togeather, Follow me on Medium Blog.**  
            
            """
        )

    # Add vertical space between columns
    st.write("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    # Content for the third column
    with col3:
        st.subheader('📉 Brand Breakdown')
        st.write(
            """
            **Explore Brand-Specific Trends**  
            Delve into detailed statistics for various car brands. Explore insights into brand popularity, market share, and performance metrics to understand how different brands are evolving.
            """
        )
        st.divider()

        st.subheader('📥 Data Download')
        st.write(
            """
            **Access Raw Data**  
            Download raw data for in-depth analysis and research. Whether you are a researcher, analyst, or enthusiast, access comprehensive datasets to support your projects and insights.
            """
        )
    
# Sidebar
st.sidebar.title('WELCOME TO WORLD OF CARS')

# Option selection from the sidebar
option = st.sidebar.selectbox(
    'CHOOSE FROM BELOW',
    ['Home', 'Search by Brand', 'Search by Category', 'EDA','DATASET','ABOUT ME']
)

# Function to handle "Search by Brand"
def search_by_brand(brand,model):
    st.title('Search by Brand')


# Load custom fonts (Montserrat and Roboto) from Google Fonts
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Roboto:ital,wght@1,300&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

    # Create two responsive columns
    c1, c2 = st.columns(2)

    import requests

    def get_youtube_videos(car_name):
        api_key = 'AIzaSyCRmnPMnqiT1NMM7pTlZBeEp2ildwe5_rw'  
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={car_name}&type=video&key={api_key}'
        response = requests.get(url)
        data = response.json()
        
        if 'items' not in data:
            print("Error:", data)
            return []

        video_ids = [item['id']['videoId'] for item in data['items']]
        video_urls = [f"https://www.youtube.com/watch?v={video_id}" for video_id in video_ids]
        return video_urls

    videos = get_youtube_videos(f"{brand} {model} official video")
    video = videos[0]
    youtube_video_id = video.split('v=')[-1]
    print(video)
    print(youtube_video_id)

    with c1: 
        autoplay_html = f"""
        <iframe width="100%" height="315" src="https://www.youtube.com/embed/{youtube_video_id}?autoplay=1&mute=0&loop=1&playlist={youtube_video_id}"
        title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        """
        st.markdown(autoplay_html, unsafe_allow_html=True)
        st.write(f"{brand}'s {model} ads from YouTube APIs")

    with c2:
        brand_taglines = {
            'Chevrolet': 'Find New Roads',
            'Toyota': "Let's Go Places",
            'Ford': 'Built Ford Tough',
            'Honda': 'The Power of Dreams',
            'Acura': 'Precision Crafted Performance',
            'Mazda': 'Feel Alive',
            'Nissan': 'Innovation that Excites',
            'Subaru': 'Love. It’s what makes a Subaru, a Subaru.',
            'BMW': 'The Ultimate Driving Machine',
            'MINI': 'Motoring Matters',
            'Pontiac': 'We Build Excitement',
            'Audi': 'Vorsprung durch Technik (Progress through Technology)',
            'Lexus': 'Experience Amazing',
            'Oldsmobile': 'Start Something',
            'Bentley': 'Be Extraordinary',
            'Jaguar': 'The Art of Performance',
            'Mitsubishi': 'Drive Your Ambition',
            'Jeep': 'Go Anywhere. Do Anything.',
            'Ferrari': 'We are the competition',
            'Mercedes-Benz': 'The Best or Nothing',
            'McLaren': 'Fearlessly Forward',
            'Porsche': 'There is No Substitute',
            'Rolls-Royce': 'Inspiration is the key',
            'Volvo': 'For Life',
            'Chrysler': 'Imported from Detroit',
            'AC': 'The Cobra, Simply the Best',
            'Alfa Romeo': 'La Meccanica delle Emozioni (The Mechanics of Emotion)',
            'Dodge': 'Domestic. Not Domesticated.',
            'FIAT': 'Driven by Passion',
            'Volkswagen': 'Das Auto (The Car)',
            'Maserati': 'Excellence through Passion',
            'Buick': 'Dream Big',
            'Triumph': 'For the Ride',
            'Cadillac': 'Dare Greatly',
            'Lamborghini': 'Expect the Unexpected',
            'INFINITI': 'Empower the Drive',
            'MG': 'The Classic Marque of Britain',
            'Saturn': 'A Different Kind of Car Company',
            'Lotus': 'For the Drivers',
            'Aston Martin': 'Power, Beauty, and Soul',
            'Saab': 'Born from Jets',
            'smart': 'Open Your Mind',
            'Plymouth': 'The Pride is Back',
            'Land Rover': 'Above and Beyond',
            'Austin-Healey': 'Built for Speed',
            'Tesla': 'Electric Cars, Solar & Clean Energy',
            'Packard': 'Ask the Man Who Owns One',
            'Excalibur': 'Elegant Motors for Exceptional People',
            'Mercury': 'New Doors Opened',
            'Kaiser': "America's First Postwar Car",
            'Sunbeam': 'Grace, Space, and Pace',
            'Datsun': 'Dare to be Different',
            'Panoz': 'Our Passion, Your Gain',
            'Suzuki': 'Way of Life!',
            'Nash': 'Give your Car a Lift',
            'Lincoln': 'American Luxury',
            'Aston': 'Power, Beauty, and Soul',
            'Scion': 'What Moves You',
            'Hyundai': 'New Thinking. New Possibilities.',
            'Kia': 'The Power to Surprise',
            'Alfa': 'La Meccanica delle Emozioni',
            'Rambler': 'Take it Easy!',
            'Bugatti': 'Ettore Bugatti',
            'Citroen': 'Inspired by You',
            'Bremen': 'A Touch of Class',
            'Austin': 'Grace, Space, Pace',
            'Polestar': 'Pure, Progressive Performance',
            'Lancia': 'The Power to Dream',
            'Delorean': 'Live the Dream',
            'Studebaker': 'First by far with a postwar car',
            'Avanti': 'The World’s Fastest Production Car',
            'DeTomaso': 'Style Never Dies',
            'Koenigsegg': 'The Spirit of Performance',
            'Eagle': 'The Premier Trail Vehicle',
            'GMC': 'We Are Professional Grade',
            'Genesis': 'Luxury Evolved',
            'Karma': 'Sustainable Luxury',
            'Lucid': 'The Future of Luxury',
            'RAM': 'Guts. Glory. Ram.',
            'VinFast': 'Boundless Together',
            'Rivian': 'Electric Adventure Vehicles',
            'Fisker': 'Revolutionary Clean Cars',
            'Isuzu': 'Go Your Own Way',
            'American Motors': 'Where quality is built in',
            'Geo': 'Get to know Geo',
            'Hummer': 'Like Nothing Else',
            'Am General': 'All American Freedom',
            'INEOS': 'Built on Purpose'
        }

        company_name = brand
        tagline = brand_taglines[brand]


        # Style the content with a white background and enhanced design
        styled_html = f"""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 315px; width: 100%; background: #FFFFFF; border-radius: 15px; padding: 20px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); overflow: hidden; position: relative;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: radial-gradient(circle at 50% 50%, rgba(0, 0, 0, 0.05) 0%, rgba(0, 0, 0, 0) 70%); animation: pulse 5s infinite; z-index: 0;"></div>
            <div style="text-align: center; margin-bottom: 20px; animation: fadeIn 1.5s ease-in-out; z-index: 1; position: relative;">
                <h1 style="font-family: 'Montserrat', sans-serif; font-size: 3.5em; color: #333333; margin: 0; text-transform: uppercase; letter-spacing: 3px; border-bottom: 3px solid #4A90E2; padding-bottom: 10px; transition: color 0.3s ease;">
                    {company_name}
                </h1>
            </div>
            <div style="text-align: center; max-width: 80%; margin: 0 auto; animation: fadeIn 2s ease-in-out; z-index: 1; position: relative;">
                <p style="font-family: 'Roboto', sans-serif; font-size: 1.5em; color: #666666; margin: 0; font-style: italic; line-height: 1.6; transition: color 0.3s ease;">
                    "{tagline}"
                </p>
            </div>
        </div>

        <style>
        @keyframes fadeIn {{
            0% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}
        @keyframes pulse {{
            0% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
            100% {{ transform: scale(1); }}
        }}
        # div:hover h1 {{
        #     color: #4A90E2;
        # }}
        # div:hover p {{
        #     color: #333333;
        # }}
        # </style>
        """
        
        st.markdown(styled_html, unsafe_allow_html=True)


    car_search_by_brand_df = df[(df['BRAND'] == brand) & ((df['CAR NAME'].str.contains(model)) | df['MODEL/CLASS'].str.contains(model))]
    years = car_search_by_brand_df['MODEL'].unique().tolist()
    years = ['ALL YEARS'] + sorted(years,reverse=True)

    selected_years = st.sidebar.multiselect(
    'Select Year(s):',
    years, 
    default=['ALL YEARS']
    )

    if selected_years == ['ALL YEARS']:
        selected_years =  years[1:]

    df_with_years = car_search_by_brand_df[(car_search_by_brand_df['MODEL'].apply(lambda x : x in selected_years))]

    state = car_search_by_brand_df[(car_search_by_brand_df['MODEL'].apply(lambda x : x in selected_years))]['DEALER LOCATION (STATE)'].unique().tolist()
    try:
        state.remove(np.nan)
    except:
        pass
    state = ['ALL STATES'] + sorted(state)
 
    selected_state = st.sidebar.multiselect(
        'Select State(s):',
        state,
        default=['ALL STATES']
    )

    if selected_state == ['ALL STATES']:
        selected_state = state[1:]
    

    df_with_years_state = df_with_years[df_with_years['DEALER LOCATION (STATE)'].apply(lambda x : x in selected_state)]

    city = car_search_by_brand_df[car_search_by_brand_df['DEALER LOCATION (STATE)'].apply(lambda x : x in selected_state)]['DEALER LOCATION (CITY)'].unique().tolist()
    city = ['ALL CITIES'] + sorted(city)

    selected_city = st.sidebar.multiselect(
        'Select City:',
        city,
        default=['ALL CITIES']
    )

    if selected_city == ['ALL CITIES']:
        selected_city = city[1:]

    
    df_with_years_state_city = df_with_years_state[df_with_years_state['DEALER LOCATION (CITY)'].apply(lambda x : x in selected_city)]
    dealer = car_search_by_brand_df[car_search_by_brand_df['DEALER LOCATION (CITY)'].apply(lambda x : x in selected_city)]['DEALER NAME'].unique().tolist()
    dealer = ['ALL DEALERS'] + dealer

    selected_dealer = st.sidebar.multiselect(
        'Select Dealer:',
        dealer,
        default=['ALL DEALERS']
    )


    final_df = df_with_years_state_city.copy()

    st.write("\n" * 10)
    st.write('-'*50)

    col1,col2 = st.columns(2)
    
    with col1:
        available_subcategory = final_df['CAR NAME'].unique().tolist()
        available_subcategory = ['SELECT ALL'] + available_subcategory
        selected_subcategory = st.selectbox('SUBCATEGORY AVALIABLE',available_subcategory,placeholder='SELECT SUBCATEGORY')

    with col2:
        subcategory_options = st.selectbox('SHOW BY',['BEST RATING','LATEST MODEL!','OLDEST MODEL!','HIGHEST PRICE','LOWEST PRICE','ONLY NEW','ONLY OLD'],placeholder='SELECT ANY ONE')
    
    st.write('\n'*10)
    st.header(f'SHOWING RESULTS BY {subcategory_options} !!')
    st.write('\n'*10)
    st.write('-'*50)

    if selected_subcategory == 'SELECT ALL':
        pass
    else:
        final_df = final_df[(final_df['CAR NAME'] == selected_subcategory)]

    if subcategory_options == 'BEST RATING':
        final_df = final_df[(final_df['RATING'] == final_df['RATING'].max())]
    elif subcategory_options == 'LATEST MODEL!':
        final_df = final_df[(final_df['MODEL'] == final_df['MODEL'].max())]
    elif subcategory_options == 'OLDEST MODEL!':
        final_df = final_df[(final_df['MODEL'] == final_df['MODEL'].min())]
    elif subcategory_options == 'HIGHEST PRICE':
        final_df = final_df[final_df['PRICE($)'] == final_df['PRICE($)'].max()]
    elif subcategory_options == 'LOWEST PRICE':
        final_df = final_df[final_df['PRICE($)'] == final_df['PRICE($)'].min()]
    elif subcategory_options == 'ONLY NEW':
        final_df = final_df[final_df['STOCK TYPE'] == 'New']
    else:
        final_df = final_df[final_df['STOCK TYPE'] == 'Used']

    
    if final_df.shape[0] == 0:
        st.subheader(f'no {subcategory_options} cars available!! search by other show by options!!')
    
    else:
        if 'current' not in st.session_state:
            st.session_state.current = 0

        if 'prev_df' not in st.session_state:
            st.session_state.prev_df = None

        # Reset current to 0 if final_df changes
        if st.session_state.prev_df is None or not final_df.equals(st.session_state.prev_df):
            st.session_state.current = 0
            st.session_state.prev_df = final_df.copy()

        def showing_details(final_df):
            
            st.header(final_df['CAR NAME'].values[0])

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric('CAR STATUS', final_df['STOCK TYPE'].values[0])
                st.metric('MAKE ORIGIN', final_df['MAKE ORIGIN'].values[0])

            with col2:
                st.metric('PRICE(USD)', final_df['PRICE($)'].values[0])
                st.metric('MILEAGE', final_df['MILEAGE'].values[0])

            with col3:
                st.metric('MODEL YEAR', str(final_df['MODEL'].values[0]))
                st.metric('CAR TYPE', final_df['CAR TYPE'].values[0])

            st.metric('PARENT COMPANY', final_df['PARENT COMPANY'].values[0])

            st.markdown(f'<a href="{final_df["IMAGE"].values[0]}" target="_blank">Click here to open the original photo of this car (photo provided by dealer/owner)</a>', unsafe_allow_html=True)

        previous, _, count, _, next = st.columns(5)

        total = final_df.shape[0]

        with previous:
                if st.button('PREVIOUS'):
                    if st.session_state.current > 0:
                        st.session_state.current -= 1
                    else:
                        st.session_state.current = total - 1  # Loop back to the last item

        with next:
                if st.button('NEXT'):
                    if st.session_state.current < total - 1:
                        st.session_state.current += 1
                    else:
                        st.session_state.current = 0  # Loop back to the first item

        with count:
            st.write(f'Showing {st.session_state.current + 1} out of {total}')

        st.write('*'*50)

        showing_details(final_df.iloc[st.session_state.current].to_frame().T)

                
            

    st.write('\n'*50)
    st.write('-'*50)
    import requests
    import random 

    def get_google_images(car_name):
        url = f"https://www.googleapis.com/customsearch/v1?q={car_name}&cx={'a1b7ef8be3781450e'}&searchType=image&key={'AIzaSyCRmnPMnqiT1NMM7pTlZBeEp2ildwe5_rw'}"
        response = requests.get(url)
        data = response.json()
        return [item['link'] for item in data.get('items', [])]

    photos = get_google_images(f'{brand} {model}')
    random.shuffle(photos)

    st.image(photos[0],f'{model}-image from google api')
    st.write('Photo Not Relevent? Refresh the Page')

    st.write('-'*50)
    
    st.header(f'ANALYSIS OF ALL {model}')


    print(selected_subcategory)

    def all_bar_charts(df):

        st.write('-'*50)
        bar1,description1 = st.columns(2)


        with bar1:
            selected1 = st.selectbox('SELECT ONE',['Price Comparison by Model Year: Overall','Price Comparison by Model Year: Used vs. New Cars'])
            st.write('\n')

        st.write('-'*50)

        with description1: 
            if selected1 == 'Price Comparison by Model Year: Overall':
                st.write('DESCRIPTION','')
                st.write('An interactive bar chart showing the average car price for each year model with prices visualized using a blue color gradient')
            else:
                st.metric('DESCRIPTION','')
                st.write('A grouped bar chart displaying the average car prices by model and stock type, with prices shown in different colors for each stock type(NEW vs OLD)')


        if selected1 == 'Price Comparison by Model Year: Overall':
                    temp1 = df.groupby('MODEL')['PRICE($)'].mean().reset_index()
                    fig1 = px.bar(temp1, x='MODEL', y='PRICE($)', text_auto=True, color='PRICE($)',
                        color_continuous_scale='Blues',  
                        title='AVERAGE PRICE BY MODEL')

                    st.plotly_chart(fig1, use_container_width=True)

        else:
            temp2 = df.groupby(['STOCK TYPE','MODEL'])['PRICE($)'].mean().unstack(level=0).fillna(0)
            fig2 = px.bar(
                    temp2,
                    x=temp2.index,
                    y=temp2.columns,
                    barmode='group',
                    text_auto=True,
                    title="AVERAGE CAR PRICE BY MODEL AND STOCK TYPE",
                    )
            fig2.update_layout(yaxis_title="Price ($)")
            st.plotly_chart(fig2,use_container_width=True)

        st.write('-'*50)

        bar2,description2 = st.columns(2)
        with bar2:
            selected2 = st.selectbox('SELECT ONE',['PRICE OF EACH SUBCATEGORY','AVG PRICE OF EACH SUBCATEGORY(NEW Vs Old)'])
        st.write('-'*50)

        with description2:
            if selected2 == 'PRICE OF EACH SUBCATEGORY':
                st.write('DESCRIPTION')
                st.write('A bar chart showing the average price of each car model, with the prices displayed in a blue color gradient')
            else:
                st.write('DESCRIPTION')
                st.write('A grouped bar chart showing the average price of each car by stock type (new vs old), with prices displayed in separate bars for each stock type')

        
        if selected2 == 'PRICE OF EACH SUBCATEGORY':
            temp3 = df.groupby('CAR NAME')['PRICE($)'].mean()
            temp3 = temp3.reset_index()
            fig3 = px.bar(
                    temp3,
                    x='CAR NAME',
                    y='PRICE($)',
                    text_auto='.2s', 
                    title="AVERAGE CAR PRICE BY CAR NAME",
                    color='PRICE($)',  
                    color_continuous_scale=px.colors.sequential.Blues, 
                )
            fig3.update_layout(yaxis_title="Price ($)")
            st.plotly_chart(fig3,use_container_width=True)
        else:
            temp4 = df.groupby(['STOCK TYPE','CAR NAME'])['PRICE($)'].mean()
            temp4 = temp4.unstack(level=0)
            temp4 = temp4.fillna(0)
            fig4 = px.bar(temp4,x=temp4.index,y=temp4.columns,barmode='group',text_auto=True,title='AVERAGE PRICE OF EACH SUBCATEGORY (NEW Vs OLD)') 
            fig4.update_layout(yaxis_title="Price ($)")
            st.plotly_chart(fig4,use_container_width=True)
        
        st.write('-'*50)
        bar3,description3 = st.columns(2)
        
        with bar3:
            selected3 = st.selectbox('SELECT ONE',['COUNT OF OLD Vs NEW CARS','COUNT OF OLD Vs NEW CARS OF EACH SUBCATEGORY'])
        st.write('-'*50)

        with description3:
            if selected3 == 'COUNT OF OLD Vs NEW CARS':
                st.write('DESCRIPTION')
                st.write('A bar chart displaying the count of old and new cars by stock type, with the counts shown as bar heights')
            else:
                st.write('DESCRIPTION')
                st.write('A grouped bar chart showing the count of old versus new cars for each car subcategory')

        if selected3 == 'COUNT OF OLD Vs NEW CARS':
                temp5 = df.groupby('STOCK TYPE')['CAR ID'].count()
                fig5 = px.bar(temp5,x=temp5.index,y=temp5.values,title='COUNT OF OLD AND NEW CARS',text_auto=True)
                fig5.update_layout(yaxis_title="COUNT OF CARS")
                st.plotly_chart(fig5,use_container_width=True)
            
        else:
                temp6 = df.groupby(['STOCK TYPE','CAR NAME'])['CAR ID'].count()
                temp6 = temp6.unstack(level=0)
                temp6 = temp6.fillna(0)
                fig6 = px.bar(temp6,x=temp6.index,y=temp6.columns,barmode='group',text_auto=True,title='COUNT OF OLD Vs NEW CARS OF EACH SUBCATEGORY')
                fig6.update_layout(yaxis_title="COUNT OF CARS")
                st.plotly_chart(fig6,use_container_width=True)

        
        st.write('-'*50)
        st.write('-'*50)
        bar4,description4 = st.columns(2)
        with bar4:
            st.selectbox('SELECT ONE',['CAR NAME PRICE AND RATING'])
        with description4:
            st.write('DESCRIPTION')
            st.write('A bar chart showing car prices by model, with the hover tooltip displaying the average rating for each car')
        avg_rating = df.groupby('CAR NAME')['RATING'].mean()
        avg_price = df.groupby('CAR NAME')['PRICE($)'].mean()

        avg_rating_ = avg_rating.reset_index()
        avg_price = avg_rating_.merge(avg_price.reset_index(),on='CAR NAME')
        avg_price['RATING'] = avg_price['RATING'].apply(lambda x : round(x,1))
        avg_price['RATING'].replace(-1,0,inplace=True)
        fig7 = px.bar(avg_price,'CAR NAME','PRICE($)',hover_name='RATING',color='CAR NAME',title='CAR NAME AND ITS PRICE AND RATING',text_auto=True)
        st.plotly_chart(fig7,use_container_width=True)
    
        
        st.write('-'*50)
        bar5,description5 = st.columns(2)
        with bar5:
           selected5 =  st.selectbox('SELECT ONE',['TOP DEALER WITH MOST NUMBER OF CARS','TOP 10 DEALER WITH MOST NUMBER OF CARS (NEW Vs OLD)'])
        with description5:
            if selected5 == 'TOP DEALER WITH MOST NUMBER OF CARS':
                st.write('DESCRIPTION')
                st.write('A bar chart showing the top dealers with the most cars available, with each bar representing the count of cars and hover text displaying the car models')
            else:
                st.write('DESCRIPTION')
                st.write('A grouped bar chart displaying the top dealers with the most cars available, categorized by stock type (new vs old), with counts shown for each category,')


        st.write('-'*50)
        if selected5 == 'TOP DEALER WITH MOST NUMBER OF CARS':
            temp8 = df.groupby(['DEALER NAME','CAR NAME'])['CAR ID'].count().sort_values(ascending=False).reset_index()
            temp8 = temp8.head(10)
            temp8 = temp8.rename(columns={'CAR ID': 'NUMBER OF CAR(s)'})
            fig8 = px.bar(temp8,x='DEALER NAME',y='NUMBER OF CAR(s)',hover_name='CAR NAME',color='CAR NAME',title='TOP DEALERS WITH MOST NUMBER OF CAR AVAILABLE',text_auto=True)
            fig8.update_layout(yaxis_title="COUNT OF CARS")
            st.plotly_chart(fig8,use_container_width=True)
        else:
            temp9 = df.groupby(['DEALER NAME','STOCK TYPE'])['CAR ID'].count().unstack(1)
            temp9 = temp9.fillna(0)
            try:
                temp9['TOTAL'] = temp9['New'] + temp9['Used']
            except:
                try:
                    temp9['TOTAL'] =  temp9['Used']
                except:
                    temp9['TOTAL'] = temp9['New']
            temp9.sort_values('TOTAL',ascending=False,inplace=True)
            temp9 = temp9.head(10)
            temp9.drop(columns='TOTAL',inplace=True)
            fig9 = px.bar(temp9,x=temp9.index,y=temp9.columns,barmode='group',title='DEALER WITH MOST NUMBER OF CARS AVAILABLE (NEW Vs OLD)',text_auto=True)
            fig9.update_layout(yaxis_title="COUNT OF CARS")
            st.plotly_chart(fig9,use_container_width=True)
        

        st.write('-'*50)
        bar6,description6 = st.columns(2)
        with bar6:
            st.selectbox('SELECT ONE ',['DEALER NAME WITH UNIQUE CARS,RATING AND PRICE'])
        with description6:
            st.write('DESCRIPTION')
            st.write('A bar chart showing the average rating of cars for each dealer, with hover text displaying the average price of the cars')
        st.write('-'*50)
        dealer_carname_count = df.groupby(['DEALER NAME','CAR NAME'])['RATING'].mean()
        dealer_carname_count = dealer_carname_count.reset_index(name='rating')
        maybe = df.groupby(['DEALER NAME','CAR NAME'])['PRICE($)'].mean()
        maybe=maybe.reset_index()
        maybe = maybe.merge(dealer_carname_count,on=['DEALER NAME','CAR NAME'])
        maybe.rating.replace(-1,0,inplace=True)
        fig10 = px.bar(maybe,'DEALER NAME','rating',hover_name='PRICE($)',color='CAR NAME',title='DEALER NAME WITH UNIQUE CAR AVAILABLE, THEIR RATING AND PRICE')
        st.plotly_chart(fig10,use_container_width=True)
    




    def all_line_charts(df):
        st.write('-'*50)
        group1,description1 = st.columns(2)
        with group1:
            select1 = st.selectbox('SELECT ONE',['AVERAGE PRICE OF CAR BY AGE (overall)','AVERAGE PRICE OF CAR (PERTICULAR MODEL)'])
        with description1:
            st.write('DESCRIPTION')
            st.write("This line chart illustrates the average car price relative to the car's age. The spline curve and markers highlight how prices tend to decrease as vehicles get older.")
        st.write('-'*50)
        
        if select1 == 'AVERAGE PRICE OF CAR (PERTICULAR MODEL)':
            with group1:
                list_of_car = df['CAR NAME'].unique().tolist()
                select1_1 = st.selectbox('SELECT ONE',list_of_car)

        if select1 == 'AVERAGE PRICE OF CAR BY AGE (overall)':
            line1 = df.groupby(['AGE OF CAR'])['PRICE($)'].mean().reset_index()
            fig = px.line(
                line1,
                x='AGE OF CAR',
                y='PRICE($)',
                markers=True,
                line_shape='spline', 
                title='Average Car Price by Age of Car',
                labels={'AGE OF CAR': 'Age of Car (Years)', 'PRICE($)': 'Average Price ($)'},
                color_discrete_sequence=['#1f77b4'], 
            )

            st.plotly_chart(fig, use_container_width=True)
        
        else:
            temp1 = df[df['CAR NAME'] == select1_1]
            line1 = temp1.groupby(['AGE OF CAR','CAR NAME'])['PRICE($)'].mean().unstack(level=1).fillna(0).reset_index()

         
            fig = px.line(
                line1,
                x='AGE OF CAR',
                y=line1.columns[1:],
                markers=True,
                line_shape='spline',
                title='Average Car Price by Age and Car Name',
                labels={'AGE OF CAR': 'Age of Car (Years)', 'value': 'Average Price ($)', 'variable': 'Car Name'},
            )

            st.plotly_chart(fig, use_container_width=True)


        st.write('-'*50)
        group2,description2 = st.columns(2)
        with group2:
            select2 = st.selectbox('SELECT ONE',['AVERAGE MILEAGE BY CAR TYPE OVER TIME'])
            # st.warning('only one stock type is available')
        with description2:
            st.write('DESCRIPTION')
            st.write("This line chart shows how average mileage varies by car type over the car's age. Each line represents a different car type, revealing trends in mileage as vehicles age.")
        st.write('-'*50)
        line2 = df.groupby(['AGE OF CAR', 'CAR TYPE'])['MILEAGE'].mean().unstack().reset_index()
        fig2 = px.line(
            line2,
            x='AGE OF CAR',
            y=line2.columns[1:], 
            markers=True,
            line_shape='linear',
            title='Average Mileage by Car Type Over Time',
            labels={'AGE OF CAR': 'Age of Car (Years)', 'value': 'Average Mileage', 'variable': 'Car Type'}
        )

        st.plotly_chart(fig2, use_container_width=True)


        st.write('-'*50)
        group3,description3 = st.columns(2)
        with group3:
            select3 = st.selectbox('SELECT ONE',['AVERAGE CAR PRICE BY DEALER LOCATION'])
            # st.warning('only one stock type is available')
        with description3:
            st.write('DESCRIPTION')
            st.write("This line chart visualizes the average car price by dealer location, distinguishing between different stock types. If only one stock type is available, the chart still displays average prices for that type, ensuring the data is presented clearly.")
        st.write('-'*50)
        line4 = df.groupby(['DEALER LOCATION (CITY)', 'STOCK TYPE'])['PRICE($)'].mean().unstack(level=1)
        line4 = line4.fillna(0)
        valid_locations = line4[(line4 > 0).sum(axis=1) > 1]

        if not valid_locations.empty and valid_locations.shape[1] > 1:
            fig4 = px.line(
                        valid_locations,
                        x=valid_locations.index,
                        y=valid_locations.columns,
                        markers=True,
                        line_shape='linear',
                        title='Average Car Price by Dealer Location',
                        labels={'DEALER LOCATION (CITY)': 'Dealer Location (City)', 'PRICE($)': 'Average Price ($)'}
                    )
            st.plotly_chart(fig4, use_container_width=True)
        else:
            line4 = df.groupby(['DEALER LOCATION (CITY)', 'STOCK TYPE'])['PRICE($)'].mean().unstack(level=1)
            line4 = line4.fillna(0)
            valid_locations = line4[(line4 > 0).sum(axis=1) > 0]

            fig4 = px.line(
                        valid_locations,
                        x=valid_locations.index,
                        y=valid_locations.columns,
                        markers=True,
                        line_shape='linear',
                        title='Average Car Price by Dealer Location',
                        labels={'DEALER LOCATION (CITY)': 'Dealer Location (City)', 'PRICE($)': 'Average Price ($)'}
                    )
            fig4.update_layout(yaxis_title="AVERAGE PRICE($)")
            st.plotly_chart(fig4, use_container_width=True)
        



        st.write('-'*50)
        group4,description4 = st.columns(2)
        with group4:
            select4 = st.selectbox('SELECT ONE',['AVERAGE CAR RATING BY SUBCATEGORY AND STOCK TYPE'])
            st.warning('NOTE : SOME DATA MAY BE LABELED AS 0 OR -1, MEANS RATING DATA IS NOT AVAILABLE!!')
        with description4:
            st.write('DESCRIPTION')
            st.write("This line chart displays the average car rating by brand and stock type, with each line representing a different stock type. It illustrates how ratings vary across car brands, providing insights into brand performance by stock category.")
        st.write('-'*50)
        
        line3 = df.groupby(['CAR NAME', 'STOCK TYPE'])['RATING'].mean().unstack(level=1).reset_index()
        st.write('-'*50)

        fig3 = px.line(
            line3,
            x='CAR NAME',
            y=line3.columns[1:],
            markers=True,
            line_shape='linear',
            title='Average Car Rating by subcategory and Stock Type',
            labels={'CAR NAME': 'Car Brand', 'RATING': 'Average Rating'}
        )
        fig3.update_layout(yaxis_title="RATINGS")

        st.plotly_chart(fig3, use_container_width=True)
        st.write('-'*50)
    
    def all_histograms(df):
        st.write('-'*50)
        group1,description1 = st.columns(2)
        with group1:
            selected1 = st.selectbox('SELECT ONE',['Distribution of Car Prices by Subcategory and Stock Type (OVERALL)','Distribution of Car Prices by Subcategory and Stock Type (NEW)','Distribution of Car Prices by Subcategory and Stock Type (USED)','SUBCATEGORYWISE DISTRIBUTION OF PRICE'])
        with description1:
            st.write('DESCRIPTION')
        st.write('-'*50)

        if selected1 == 'Distribution of Car Prices by Subcategory and Stock Type (OVERALL)':
            with description1:
                st.write("This histogram showcases the overall distribution of car prices, categorized by subcategory and stock type. It highlights price variations across different subcategory and stock categories, offering insights into the overall pricing landscape.")
            fig1 = px.histogram(df,'PRICE($)',text_auto=True,color='CAR NAME',pattern_shape='STOCK TYPE',title='Distribution of Car Prices by subcategory and Stock Type (OVERALL)')
            st.plotly_chart(fig1,use_container_width=True)

        elif selected1 == 'Distribution of Car Prices by Subcategory and Stock Type (NEW)':
            with description1:
                st.write("This histogram illustrates the distribution of prices for new cars, categorized by subcategory and stock type. It provides a focused view of how prices vary among new vehicles across different subcateogory.")
            hist = df[df['STOCK TYPE'] == 'New']
            fig2 = px.histogram(hist,'PRICE($)',text_auto=True,color='CAR NAME',pattern_shape='STOCK TYPE',title='Distribution of Car Prices by subcategory and Stock Type (NEW)')
            st.plotly_chart(fig2,use_container_width=True)
        
        elif selected1 == 'SUBCATEGORYWISE DISTRIBUTION OF PRICE':
            with group1:
                selected1_1 = st.selectbox('SELECT SUBCATEGORY',df['CAR NAME'].unique().tolist())
            with description1:
                st.write("This histogram presents the price distribution for a specific car subcategory, broken down by stock type. It offers a detailed look at how prices vary within the selected subcategory, highlighting differences between new and used vehicles.")
            
            hist = df[df['CAR NAME'] == selected1_1]
            fig3 = px.histogram(hist,'PRICE($)',text_auto=True,color='CAR NAME',pattern_shape='STOCK TYPE',title=f'Distribution of {selected1_1} Prices by Stock Type')
            st.plotly_chart(fig3,use_container_width=True)
        
        else:
            with description1:
                st.write("This histogram displays the price distribution for used cars, categorized by subcategory and stock type. It highlights how used car prices differ across various subcategory, offering insights into the secondhand market.")
            hist = df[df['STOCK TYPE'] == 'Used']
            fig4 = px.histogram(hist,'PRICE($)',text_auto=True,color='CAR NAME',pattern_shape='STOCK TYPE',title='Distribution of Car Prices by subcategory and Stock Type (USED)')
            st.plotly_chart(fig4,use_container_width=True)

        
        st.write('-'*50)
        group2,description2 = st.columns(2)
        with group2:
            selected2 = st.selectbox('SELECT ONE',['MILEAGE Vs PRICE($) - ALL USED','MILEAGE Vs PRICE($) - SUBCATEGORY WISE USED'])
        with description2:
            st.write('DESCRIPTION')
        st.write('-'*50)

        hist = df[df['STOCK TYPE'] == 'Used']
        if selected2 == 'MILEAGE Vs PRICE($) - ALL USED':
            with description2:
                st.write("This histogram shows the relationship between mileage and average price for all used cars, categorized by subcategory. It provides insights into how mileage impacts the pricing of used vehicles across different subcategory.")
            fig5 = px.histogram(hist,'MILEAGE',y='PRICE($)',color='CAR NAME',histfunc='avg',text_auto=True,title='MILEAGE Vs PRICE($) OF ALL USED CARS')
            st.plotly_chart(fig5,use_container_width=True)
        else:
            with group2:
                selected2_2 = st.selectbox('SELECT SUBCATEGORY',hist['CAR NAME'].unique().tolist())
            with description2:
                st.write("This histogram focuses on the relationship between mileage and average price for a specific used car subcategory. It highlights how mileage influences the pricing of used vehicles within the selected subcategory.")
            hist_ = hist[hist['CAR NAME'] == selected2_2]
            fig6 = px.histogram(hist_,'MILEAGE',y='PRICE($)',color='CAR NAME',histfunc='avg',text_auto=True,title=f'MILEAGE Vs PRICE($) OF ALL USED {selected2_2}')
            st.plotly_chart(fig6,use_container_width=True)
        

        st.write('-'*50)
        group3,description3 = st.columns(2)
        with group3:
            selected3 = st.selectbox('SELECT ONE',['RATING Vs AVG PRICE - overall','RATING Vs AVG PRICE - old','RATING Vs AVG PRICE - new'])
            
        with description3:
            st.write('DESCRIPTION')
        st.write('-'*50)

        if selected3 == 'RATING Vs AVG PRICE - overall':
            with description3:
                st.write("This histogram visualizes the relationship between car ratings and average prices, categorized by subcategory and stock type. It offers insights into how customer ratings correlate with the pricing of different car subcategory and stock categories.")
            fig7 = px.histogram(df,'RATING',y='PRICE($)',color='CAR NAME',pattern_shape='STOCK TYPE',histfunc='avg',text_auto=True)
            st.plotly_chart(fig7,use_container_width=True)
        elif selected3 == 'RATING Vs AVG PRICE - old':
            with description3:
                st.write("This histogram shows the correlation between car ratings and average prices specifically for used cars, categorized by subcategory. It provides insights into how ratings influence the pricing of used vehicles across different subcategory.")
            df_ = df[df['STOCK TYPE'] == 'Used']
            fig8 = px.histogram(df_,'RATING',y='PRICE($)',color='CAR NAME',pattern_shape='STOCK TYPE',histfunc='avg',text_auto=True)
            st.plotly_chart(fig8,use_container_width=True)
        else:
            with description3:
                st.write("This histogram explores the relationship between car ratings and average prices for new cars, categorized by subcategory. It highlights how ratings impact the pricing of new vehicles across different subcategory.")
            df_ = df[df['STOCK TYPE'] == 'New']
            fig8 = px.histogram(df_,'RATING',y='PRICE($)',color='CAR NAME',pattern_shape='STOCK TYPE',histfunc='avg',text_auto=True)
            st.plotly_chart(fig8,use_container_width=True)
        st.write('-'*50)
        
    
    def all_piecharts(df):
        st.write('-'*50)
        group1,description1 = st.columns(2)
        with description1:
            for i in range(3):
                st.write('|')
            st.write('| DESCRIPTION')
            st.write("| This pie chart illustrates the percentage distribution of new versus used cars. It visually represents how the car stock is divided between these two categories, providing a clear comparison of their proportions.")
            for i in range(3):
                st.write('|')


        with group1:
            fig = px.pie(df,'STOCK TYPE',title='PERCENTAGE OF NEW Vs. USED CARS')
            fig.update_traces(textinfo = 'percent+label')
            st.plotly_chart(fig,use_container_width=True)

        
        st.write('-'*50)


        group2,description2 = st.columns(2)
        with group2:
            fig = px.pie(df,'PRICE RANGE',title='PRICE RANGE OF CAR')
            fig.update_traces(textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)

        with description2:
            for i in range(3):
                st.write('|')
            st.write('| DESCRIPTION')
            st.write("| This pie chart presents the distribution of cars across different price ranges. It highlights the proportion of vehicles available within each price category, offering a clear view of the pricing landscape.")
            for i in range(3):
                st.write('|')
        
        st.write('-'*50)
            
        group_,description_ = st.columns(2)
        with group_:
            temp3 = df.groupby(['CAR NAME'])['PRICE($)'].mean()
            fig = px.pie(temp3,values=temp3.values,names=temp3.index)
            st.plotly_chart(fig,use_container_width=True)

        with description_:
            for i in range(3):
                st.write('|')
            st.write('| DESCRIPTION')
            st.write("| This pie chart highlights the average price distribution across different car subcategory. It offers a quick comparison of how various subcategory are positioned in terms of their average pricing.")
            for i in range(3):
                st.write('|')

        st.write('-'*50)

        group3,description3 = st.columns(2)
        with group3:
            pie1 = df.groupby('DEALER NAME')['CAR ID'].count().sort_values(ascending=False).head(10)
            fig = px.pie(pie1,pie1.values,hover_name=pie1.index,title='COUNT OF CAR WITH EACH DEALERS')
            fig.update_traces(textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)

        with description3:
            for i in range(3):
                st.write('|')
            st.write('| DESCRIPTION')
            st.write("| This pie chart displays the top 10 dealers by the number of cars they have available. It highlights the proportion of cars each dealer holds, providing insights into the largest contributors in the market.")
            for i in range(3):
                st.write('|')

        st.write('-'*50)
            
        group4,description4 = st.columns(2)
        with group4:
            fig = px.pie(df,'CAR TYPE',title='CAR TYPE')
            st.plotly_chart(fig,use_container_width=True)

        with description4:
            for i in range(3):
                st.write('|')
            st.write('| DESCRIPTION')
            st.write("| This pie chart shows the distribution of different car types in the dataset. It reveals the proportion of each car type, offering insights into the variety of vehicles available.")
            for i in range(3):
                st.write('|')


        st.write('-'*50)
        st.write('DESCRIPTION')
        st.write("This pie chart represents the distribution of car prices by subcategory, with colors indicating the age of the cars. It visually combines subcategory, price, and car age to provide a comprehensive overview.")

        fig = px.pie(df,
                    names='CAR NAME',
                    values='PRICE($)',
                    color='AGE OF CAR',
                    title='CAR NAME | PRICE | AGE OF CAR')
        fig.update_traces(textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)


        st.write('-'*50)
        
        st.write('DESCRIPTION')
        st.write("This pie chart illustrates the distribution of cars by their age. It provides a clear visual representation of the proportion of cars within each age group.")
        fig = px.pie(df,'AGE OF CAR',title='AGE OF CAR')
        fig.update_traces(textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

        st.write('-'*50)

        st.write('DESCRIPTION')
        st.write("This pie chart displays the distribution of car subcategory, with segments representing the count of cars for each subcategory. Hovering over each segment reveals the mean price of cars within that subcategory.")
        pie2 = df.groupby(['CAR NAME']).agg(
            count = ('CAR NAME','size'),
            mean_price = ('PRICE($)','mean')
        )
        fig = px.pie(pie2,pie2.index,hover_data={'mean_price'},values='count',title='CAR NAME | COUNT | MEAN PRICE')
        fig.update_traces(textinfo='label')
        st.plotly_chart(fig,use_container_width=True)

        st.write('-'*50)

        st.write('DESCRIPTION')
        st.write("This pie chart shows the distribution of car models by year. It provides a breakdown of the proportion of each model year.")
        fig = px.pie(df,'MODEL',title='CAR MODEL YEAR DISTRIBUTION')
        fig.update_traces(textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

        st.write('-'*50)
    
    def all_treemap(df):
        df.dropna(inplace=True)
        st.write('-'*50)
        st.write('DESCRIPTION')
        st.write("This treemap visualizes car prices, segmented by stock type, car name, and model year. It offers a hierarchical view of pricing across different categories.")
        fig = px.treemap(df,path=[px.Constant(model),'STOCK TYPE','CAR NAME','MODEL'],values='PRICE($)',title='Hierarchical Pricing Distribution: Model, Stock Type, and Car Name')
        st.plotly_chart(fig,use_container_width=True)
        st.write('-'*50)

        st.write('DESCRIPTION')
        st.write("This treemap visualizes the hierarchical distribution of car prices, segmented by stock type, model, and dealer name. It provides a detailed view of pricing across different categories and locations.")
        fig = px.treemap(df,path=[px.Constant(model),'STOCK TYPE','MODEL','DEALER NAME'],hover_data={'DEALER LOCATION (STATE)':True,'DEALER LOCATION (CITY)':True},title='Hierarchical Distribution of Car Prices by Stock Type, Model, and Dealer Name')
        st.plotly_chart(fig,use_container_width=True)
        st.write('-'*50)

        st.write('DESCRIPTION')
        st.write("This treemap displays the hierarchical distribution of mean car prices, categorized by dealer, location, stock type, model, and car name. It helps visualize pricing trends and comparisons across different levels of the hierarchy.")
        mean_prices = df.groupby(['DEALER NAME', 'DEALER LOCATION (STATE)', 'STOCK TYPE', 'MODEL','CAR NAME'])['PRICE($)'].mean().reset_index()
        fig = px.treemap(mean_prices,path=[px.Constant(model),'DEALER NAME','DEALER LOCATION (STATE)','STOCK TYPE','MODEL','CAR NAME'],values='PRICE($)',title="Hierarchical Distribution of Mean Car Prices by Dealer, Location, Stock Type, Model, and Car Name")
        st.plotly_chart(fig,use_container_width=True)
        st.write('-'*50)
    
    def all_sunbrust(df):
        df.dropna(inplace=True)
        
        st.write('-'*50)
        st.write('DESCRIPTION')
        st.write("This sunburst chart illustrates the hierarchical distribution of dealers by model/class, state, city, and dealer name. It provides an interactive way to explore relationships and data within each hierarchical level.")
        fig = px.sunburst(df,path=['MODEL/CLASS','DEALER LOCATION (STATE)','DEALER LOCATION (CITY)','DEALER NAME'],title='Hierarchical Distribution of class, location(city), location(state), dealer name')
        st.plotly_chart(fig,use_container_width=True)
        st.write('-'*50)

        st.write('DESCRIPTION')
        st.write("This sunburst chart visualizes the distribution of car counts, categorized by dealer name, stock type, and car name. It effectively showcases how car counts are distributed across different dealers and stock types.")
        dealer_car = df.groupby('DEALER NAME')['CAR ID'].count().sort_values(ascending=False)
        index = dealer_car.head(10).index
        truevalues = df[df['DEALER NAME'].apply(lambda x : True if x in index else False)]
        truevalues = truevalues.groupby(['MODEL/CLASS','DEALER NAME','STOCK TYPE','CAR NAME'])['CAR ID'].count().reset_index(name='COUNT OF CARS')
        fig = px.sunburst(truevalues,path=['DEALER NAME','STOCK TYPE','CAR NAME'],values='COUNT OF CARS',title='Car Distribution by Dealer Name, Stock Type, and Car Model')
        st.plotly_chart(fig,use_container_width=True)
        st.write('-'*50)

        st.write("DESCRIPTION")
        st.write("This sunburst chart displays the average car price distribution across different model/classes, stock types, car names, and models. It provides a hierarchical view of pricing trends and variations.")
        temp_ = df.groupby(['MODEL/CLASS','STOCK TYPE','CAR NAME','MODEL'])['PRICE($)'].mean()
        temp_ = temp_.reset_index()
        fig = px.sunburst(temp_, path=['MODEL/CLASS','STOCK TYPE','CAR NAME','MODEL'],values='PRICE($)',title="Average Car Price Distribution by Model/Class, Stock Type, Car Name, and Model")
        st.plotly_chart(fig,use_container_width=True)
        st.write('-'*50)
    
    def all_bubble(df):

        st.write('-'*50)
        group1,description1 = st.columns(2)
        with description1:
            st.write('DESCRIPTION')
        with group1:
            select1 = st.selectbox('SELECT ONE',['MILEAGE Vs. PRICE (OVERALL)','MILEAGE Vs. PRICE (USED)','MILEAGE Vs. PRICE (SUBCATEGORY WISE)'])
        
        if select1 == 'MILEAGE Vs. PRICE (OVERALL)':
           with description1:
               st.write("This scatter plot illustrates the relationship between car mileage and price, color-coded by car brand and differentiated by stock type. The size of each point represents the car's age, providing insights into how these factors interact.")
           fig = px.scatter(df,'MILEAGE','PRICE($)',color='CAR NAME',symbol='STOCK TYPE',size='AGE OF CAR',title='Mileage vs. Price of Cars by Brand and Stock Type (OVERALL)')
           st.plotly_chart(fig,use_container_width=True)

        elif select1 == 'MILEAGE Vs. PRICE (USED)':
            with description1:
                st.write(" This scatter plot shows the relationship between mileage and price for used cars, with color representing different car brands and size indicating the car's age. It provides insights into pricing trends and mileage across various brands.")
            used = df[df['STOCK TYPE'] == 'Used']
            fig = px.scatter(used,'MILEAGE','PRICE($)',color='CAR NAME',symbol='STOCK TYPE',size='AGE OF CAR',title='Mileage vs. Price of Cars by Brand and Stock Type (USED)')
            st.plotly_chart(fig,use_container_width=True)
        
        else:
            with description1:
                st.write("This scatter plot illustrates the relationship between mileage and price for a selected car subcategory, with points sized by the car's age and colored by stock type. It provides a focused view of how mileage and price vary for a specific subcategory.")
            with group1:
                select1_1 = st.selectbox('SELECT ONE',df['CAR NAME'].unique().tolist())
            perticular_car = df[df['CAR NAME'] == select1_1]
            fig = px.scatter(perticular_car,'MILEAGE','PRICE($)',color='CAR NAME',symbol='STOCK TYPE',size='AGE OF CAR',title=f"Mileage vs. Price for {select1_1}")
            st.plotly_chart(fig,use_container_width=True)
        
        
        st.write('-'*50)
        group2,description2 = st.columns(2)
        with description2:
            st.write('DESCRIPTION')
        with group2:
            select2 = st.selectbox('SELECT ONE',['MILEAGE Vs. PRICE with RATING (OVERALL)','MILEAGE Vs. PRICE with RATING (SUBCATEGORY WISE)'])

        df['RATING'].replace(-1,0,inplace=True)
        if select2 == 'MILEAGE Vs. PRICE with RATING (OVERALL)':
            with description2:
                st.write("This scatter plot visualizes the relationship between price and mileage, with point size indicating rating and color representing car subcategoreis. It also differentiates between new and used cars, providing a detailed overview of these variables.")
            fig = px.scatter(df,'PRICE($)','MILEAGE',size='RATING',color='CAR NAME',facet_col='STOCK TYPE',hover_data={'MODEL':True})
            st.plotly_chart(fig,use_container_width=True)
        else:
            with description2:
                st.write("This scatter plot illustrates the price versus mileage for a selected car subcategory, with point size representing the rating and color indicating the car subcategory. It also separates the data by stock type (new or used), offering insights into different segments.")
            with group2:
                select2_2 = st.selectbox('SELECT SUBCATEGORY',df['CAR NAME'].unique().tolist())
            perticular_car = df[df['CAR NAME'] == select2_2]
            fig = px.scatter(perticular_car,'PRICE($)','MILEAGE',size='RATING',color='CAR NAME',facet_col='STOCK TYPE',hover_data={'MODEL':True},title="Price vs. Mileage for Selected Car subcategory with Stock Type Breakdown")
            st.plotly_chart(fig,use_container_width=True)
        st.write('-'*50)

        group3,description3 = st.columns(2)
        with group3:
            select = st.selectbox('SELECT ONE',['COUNT OF CARS WITH EACH DEALER'])
        with description3:
            st.write('DESCRIPTION')
            st.write("This bubble plot represents the count of cars for each dealer. The bubble sizes indicate car counts, with colors distinguishing between different stock types for clear comparison across dealerships.")
        bubble1 = df.groupby(['DEALER NAME','CAR NAME','STOCK TYPE'])['CAR ID'].count().reset_index(name='COUNT')
        fig = px.scatter(bubble1,y='CAR NAME',x='DEALER NAME',size='COUNT',color='STOCK TYPE',title='COUNT OF CARS WITH EACH DEALER')
        st.plotly_chart(fig,use_container_width=True)
    
    def all_scatter(df):
        
        st.write('-'*50)
        group1,description1 = st.columns(2)
        with group1:
            select1 = st.selectbox('SELECT ONE',['RATING Vs. PRICE - OVERALL','RATING Vs. PRICE - NEW CAR','RATING Vs. PRICE - USED CAR'])
        with description1:
            st.write('DESCRIPTION')
        
        if select1 == 'RATING Vs. PRICE - OVERALL':
            with description1:
                st.write("This scatter plot visualizes the relationship between car ratings and prices. Different car names are color-coded, and stock types are distinguished using symbols for clearer comparison.")
            fig = px.scatter(df,'RATING','PRICE($)',color='CAR NAME',symbol='STOCK TYPE',title='RELATION BETWEEN RATING AND PRICE')
            st.plotly_chart(fig,use_container_width=True)
        elif select1 == 'RATING Vs. PRICE - NEW CAR':
            with description1:
                st.write("This scatter plot highlights the relationship between ratings and prices of new cars. Car names are color-coded, with stock types differentiated by symbols for better insights.")
            temp_ = df[df['STOCK TYPE'] == 'New']
            fig = px.scatter(temp_,'RATING','PRICE($)',color='CAR NAME',symbol='STOCK TYPE',title='RELATION BETWEEN RATING AND PRICE OF NEW CARS')
            st.plotly_chart(fig,use_container_width=True)
        else:
            with description1:
                st.write("This scatter plot shows the relationship between ratings and prices of used cars. Different car names are color-coded, with stock types represented by distinct symbols for easy comparison.")
            temp_ = df[df['STOCK TYPE'] == 'Used']
            fig = px.scatter(temp_,'RATING','PRICE($)',color='CAR NAME',symbol='STOCK TYPE',title='RELATION BETWEEN RATING AND PRICE OF USED CARS')
            st.plotly_chart(fig,use_container_width=True)
        st.write('-'*50)
    
    def all_box(df):
        st.write('-'*50)
        group1,description1 = st.columns(2)
        with group1:
            selected1 = st.selectbox('SELECT ONE',['DESTRIBUTION OF CAR PRICE BY MODEL (OVERALL)','DESTRIBUTION OF CAR PRICE BY MODEL (NEW Vs. USED)'])
        with description1:
            st.write('DESCRIPTION')
        st.write('-'*50)
        
        if selected1 == 'DESTRIBUTION OF CAR PRICE BY MODEL (OVERALL)':
            with description1:
                st.write("This box plot displays car prices across different models, illustrating the distribution of prices for each car model.")
            fig = px.box(df,y='PRICE($)',x='CAR NAME',title='CAR PRICE BY MODEL')
            st.plotly_chart(fig,use_container_width=True)
        else:
            with description1:
                st.write("This box plot compares car prices by model, distinguishing between new and used vehicles. Each car model is color-coded by stock type, allowing for a clear comparison of price distributions.")
            fig = px.box(df,y='PRICE($)',x='CAR NAME',color='STOCK TYPE',title='CAR PRICE BY MODEL (NEW Vs. USED)')
            st.plotly_chart(fig,use_container_width=True)
        
        st.write('-'*50)
        group2,description2 = st.columns(2)
        with group2:
            selected2 = st.selectbox('SELECT ONE',['PRICE OF NEW Vs OLD MODEL (OVERALL)','PRICE OF NEW Vs. OLD MODEL (SUBCATEGORY-WISE)'])
        with description2:
            st.write("DESCRIPTION")
        st.write('-'*50)
        
        if selected2 == 'PRICE OF NEW Vs OLD MODEL (OVERALL)':
            with description2:
                st.write("This box plot visualizes the distribution of car prices based on stock type, providing insights into price variations between new and used cars.")
            fig = px.box(df,y='PRICE($)',x='STOCK TYPE',title='PRICE OF NEW Vs. OLD MODEL (OVERALL)')
            st.plotly_chart(fig,use_container_width=True)
        else:
            with description2:
                st.write("This box plot shows car price distributions by stock type, with each car model color-coded. It highlights price variations within new and used cars across different models.")
            fig = px.box(df,y='PRICE($)',x='STOCK TYPE',color='CAR NAME',title="PRICE OF NEW Vs. OLD MODEL OF EACH SUBCATEGORY")
            st.plotly_chart(fig,use_container_width=True)
            
        st.write('-'*50)
        group3,description3 = st.columns(2)
        with group3:
            selected3 = st.selectbox('SELECT ONE',['Spread of mileage of Used car models (OVERALL)','Spread of mileage across Used car models (SUBCATEGORY-WISE)'])
        with description3:
            st.write("DESCRIPTION")
        
        if selected3 == 'Spread of mileage of Used car models (OVERALL)':
            with description3:
                st.write("This box plot visualizes the distribution of mileage for used car models, showcasing the range and spread of mileage values across different vehicles.")
            box1 = df[df['STOCK TYPE'] == 'Used']
            fig = px.box(box1,'MILEAGE',title='SPREAD OF MILEAGE OF USED CAR MODELS')
            st.plotly_chart(fig,use_container_width=True)
        else:
           with description3:
            st.write("This box plot displays the distribution of mileage across different used car models, providing insights into the mileage spread for each car name.")
           box1 = df[df['STOCK TYPE'] == 'Used']
           fig = px.box(box1,'CAR NAME','MILEAGE')
           st.plotly_chart(fig,use_container_width=True)
        st.write('-'*50)
    
    def all_cartograpic(df):

        us_states = json.load(open("us-states.json", "r"))

        df.dropna(inplace=True)
        df = df[df['RATING'] != -1]

        state_id_map = {'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'}

        st.write('-'*50)

        group1,description1 = st.columns(2)
        with group1:
            select1 = st.selectbox("SELECT ONE",['OVERALL RATING','NEW CARS','USED CARS','SPECIFIC MODEL'])
        with description1:
            if select1 == 'OVERALL RATING':
                st.write('DESCRIPTION')
                st.write("Explore state-wise car ratings across the U.S. using an interactive map. The Map includes Alaska and Hawaii, with ratings color-coded for clarity.")
            elif select1 == 'NEW CARS':
                st.write('DESCRIPTION')
                st.write("Discover state-wise ratings for new cars across the U.S., with an interactive map highlighting each state. This view includes Alaska and Hawaii, showcasing ratings in an easily interpretable format.")
            elif select1 == 'USED CARS':
                st.write('DESCRIPTION')
                st.write("Explore the state-wise ratings for used cars across the U.S. using an interactive map. This visualization includes all states, offering a clear comparison of ratings from coast to coast.")
        st.write('-'*50)
            
        df['id'] = df['DEALER LOCATION (STATE)'].apply(lambda x :state_id_map[x])

        if select1 == 'OVERALL RATING':
            grouped_df = df.groupby('id').agg(
            mean_rating=('RATING', 'mean'),
            state=('DEALER LOCATION (STATE)', 'first')
            ).reset_index()
            grouped_df['mean_rating'] = round(grouped_df['mean_rating'],1)

            fig = px.choropleth_mapbox(
                grouped_df,
                locations="id",
                geojson=us_states,
                color="mean_rating",
                hover_name="state",
                hover_data=["mean_rating"],
                title="STATE WISE RATING",
                mapbox_style="carto-positron",
                center={"lat": 37.0902, "lon": -95.7129}, 
                zoom=2,
                opacity=0.6
            )

            fig.update_layout(
                mapbox_bounds={"west": -179, "east": -60, "south": 18, "north": 72},  # Adjusted bounds to include Alaska and Hawaii
                margin={"r": 0, "t": 50, "l": 0, "b": 0}  # Remove default margins
            )

            st.plotly_chart(fig, use_container_width=True)

        elif select1 == 'NEW CARS':
            df_new1 = df[df['STOCK TYPE'] == 'New']
            grouped_df = df_new1.groupby('id').agg(
            mean_rating=('RATING', 'mean'),
            state=('DEALER LOCATION (STATE)', 'first')
            ).reset_index()
            grouped_df['mean_rating'] = round(grouped_df['mean_rating'],1)

            fig = px.choropleth_mapbox(
                grouped_df,
                locations="id",
                geojson=us_states,
                color="mean_rating",
                hover_name="state",
                hover_data=["mean_rating"],
                title="STATE WISE RATING OF NEW CARS",
                mapbox_style="carto-positron",
                center={"lat": 37.0902, "lon": -95.7129}, 
                zoom=2,
                opacity=0.6
            )

            fig.update_layout(
                mapbox_bounds={"west": -179, "east": -60, "south": 18, "north": 72},
                margin={"r": 0, "t": 50, "l": 0, "b": 0}  # Increase the top margin to allow space for the title
            )
            

            st.plotly_chart(fig, use_container_width=True)
        
        elif select1 == 'USED CARS':

            df_used1 = df[df['STOCK TYPE'] == 'Used']
            grouped_df = df_used1.groupby('id').agg(
            mean_rating=('RATING', 'mean'),
            state=('DEALER LOCATION (STATE)', 'first')
            ).reset_index()
            grouped_df['mean_rating'] = round(grouped_df['mean_rating'],1)

            fig = px.choropleth_mapbox(
                grouped_df,
                locations="id",
                geojson=us_states,
                color="mean_rating",
                hover_name="state",
                hover_data=["mean_rating"],
                title="STATE WISE RATING OF USED CARS",
                mapbox_style="carto-positron",
                center={"lat": 37.0902, "lon": -95.7129}, 
                zoom=2,
                opacity=0.6
            )

            fig.update_layout(
                mapbox_bounds={"west": -179, "east": -60, "south": 18, "north": 72},  # Adjusted bounds to include Alaska and Hawaii
                margin={"r": 0, "t": 50, "l": 0, "b": 0}  # Remove default margins
            )

            st.plotly_chart(fig, use_container_width=True)
        
        else:
            with group1:
                select1_1 = st.selectbox('SELECT ONE',df['CAR NAME'].unique())
            with description1:
                select1_1_1 = st.selectbox('SELECT ONE',['OVER ALL','NEW CARS','USED CARS'])
                st.write('DESCRIPTION')
                st.write(f"View state-wise ratings for {select1_1} the U.S., with an interactive map highlighting ratings.")
            
            if select1_1_1 == 'NEW CARS':
                specific_new1 = df[(df['CAR NAME'] == select1_1) & (df['STOCK TYPE'] == 'New')]
                grouped_df = specific_new1.groupby('id').agg(
                mean_rating=('RATING', 'mean'),
                state=('DEALER LOCATION (STATE)', 'first')
                ).reset_index()
                grouped_df['mean_rating'] = round(grouped_df['mean_rating'],1)
            elif select1_1_1 == 'USED CARS':
                specific_used1 = df[(df['CAR NAME'] == select1_1) & (df['STOCK TYPE'] == 'Used')]
                grouped_df = specific_used1.groupby('id').agg(
                mean_rating=('RATING', 'mean'),
                state=('DEALER LOCATION (STATE)', 'first')
                ).reset_index()
                grouped_df['mean_rating'] = round(grouped_df['mean_rating'],1)
            else:
                specific_overall1 = df[df['CAR NAME'] == select1_1]
                grouped_df = specific_overall1.groupby('id').agg(
                mean_rating=('RATING', 'mean'),
                state=('DEALER LOCATION (STATE)', 'first')
                ).reset_index()
                grouped_df['mean_rating'] = round(grouped_df['mean_rating'],1)


            fig = px.choropleth_mapbox(
                grouped_df,
                locations="id",
                geojson=us_states,
                color="mean_rating",
                hover_name="state",
                hover_data=["mean_rating"],
                title=f"STATE WISE RATING OF {select1_1} CARS",
                mapbox_style="carto-positron",
                center={"lat": 37.0902, "lon": -95.7129}, 
                zoom=2,
                opacity=0.6
            )

            fig.update_layout(
                mapbox_bounds={"west": -179, "east": -60, "south": 18, "north": 72},  # Adjusted bounds to include Alaska and Hawaii
                margin={"r": 0, "t": 50, "l": 0, "b": 0}  # Remove default margins
            )

            st.plotly_chart(fig, use_container_width=True)

        st.write('-'*50)

        group2,description2 = st.columns(2)
        with group2:
            select2 = st.selectbox("SELECT ONE",['OVERALL COUNT','NEW CARS','USED CARS','SPECIFIC MODEL'])
        with description2:
            if select2 == 'OVERALL COUNT':
                st.write('DESCRIPTION')
                st.write("Explore the distribution of car counts across U.S. states with this interactive map. The visualization highlights the number of cars per state, offering insights into car density nationwide.")
            elif select2 == 'NEW CARS':
                st.write('DESCRIPTION')
                st.write("Explore the distribution of new cars across U.S. states with an interactive map. Hover over states to view car counts and see the overall distribution visually.")
            elif select2 == 'USED CARS':
                st.write('DESCRIPTION')
                st.write("Explore the distribution of used cars across U.S. states with this interactive map. Hover over each state to see the number of used cars available.")
            else:
                select2_2_2 = st.selectbox('SELECT ONE',['OVERALL COUNT','NEW CARS','USED CARS'])
                st.write('DESCRIPTION')
                st.write("Explore the distribution of specific cars across the U.S. with an interactive map showing the number of cars per state. The map highlights state-wise counts using a clear color gradient for easy comparison.")
        st.write('-'*50)
                
        
        if select2 == 'NEW CARS':
            df_new = df[df['STOCK TYPE'] == 'New']
            car_count = df_new.groupby('id').agg(cars_count = ('CAR ID','count'),
                                   state = ('DEALER LOCATION (STATE)','first')).reset_index()
        elif select2 == 'USED CARS':
            df_used = df[df['STOCK TYPE'] == 'Used']
            car_count = df_used.groupby('id').agg(cars_count = ('CAR ID','count'),
                                   state = ('DEALER LOCATION (STATE)','first')).reset_index()
        elif select2 == 'SPECIFIC MODEL':
          with group2:
            select2_2 = st.selectbox('SELECT ONE',df['CAR NAME'].unique())
          if select2_2_2 == 'OVERALL COUNT':
              specific_overall = df[df['CAR NAME'] == select2_2]
              car_count = specific_overall.groupby('id').agg(cars_count = ('CAR ID','count'),
                                   state = ('DEALER LOCATION (STATE)','first')).reset_index()
          elif select2_2_2 == 'NEW CARS':
              specific_new = df[(df['CAR NAME'] == select2_2) & (df['STOCK TYPE'] == 'New')]
              car_count = specific_new.groupby('id').agg(cars_count = ('CAR ID','count'),
                                   state = ('DEALER LOCATION (STATE)','first')).reset_index()
          else:
              specific_used = df[(df['CAR NAME'] == select2_2) & (df['STOCK TYPE'] == 'Used')]
              car_count = specific_used.groupby('id').agg(cars_count = ('CAR ID','count'),
                                   state = ('DEALER LOCATION (STATE)','first')).reset_index()
        else:
            car_count = df.groupby('id').agg(cars_count = ('CAR ID','count'),
                                   state = ('DEALER LOCATION (STATE)','first')).reset_index()
            
        fig = px.choropleth_mapbox(
            car_count,
            geojson=us_states,
            locations='id',
            color='cars_count',
            hover_name='state', 
            hover_data={'cars_count': True}, 
            mapbox_style="carto-positron",
            center={"lat": 38, "lon": -96.5},  
            zoom=2,  
            opacity=0.5,
            title= "Car Distribution by State in USA"
        )

        fig.update_layout(
                mapbox_bounds={"west": -179, "east": -60, "south": 18, "north": 72},  # Adjusted bounds to include Alaska and Hawaii
                margin={"r": 0, "t": 50, "l": 0, "b": 0}  # Remove default margins
            )
        st.plotly_chart(fig, use_container_width=True)
        st.write('-'*50)
        



        group3,description3 = st.columns(2)
        with group3:
            select3 = st.selectbox("SELECT ONE.",['OVERALL PRICE','NEW CARS','USED CARS','SPECIFIC MODEL'])
        
        if select3 == 'NEW CARS':
            with description3:
                st.write('DESCRIPTION')
                st.write("Examine the distribution of new car prices across the U.S. with an interactive map displaying average prices by state. The map highlights price variations, including Alaska and Hawaii, for comprehensive insights.")
            df_new3 = df[df['STOCK TYPE'] == 'New']
            car_price = df_new3.groupby(['id']).agg(mean_price = ('PRICE($)','mean'),
                                     state = ('DEALER LOCATION (STATE)','first')).reset_index()
            car_price['mean_price'] = round(car_price['mean_price'])

        elif select3 == 'USED CARS':
            with description3:
                st.write('DESCRIPTION')
                st.write("Examine the distribution of used car prices across the U.S. with an interactive map displaying average prices by state. The map highlights price variations, including Alaska and Hawaii, for comprehensive insights.")
            df_used3 = df[df['STOCK TYPE'] == 'Used']
            car_price = df_used3.groupby(['id']).agg(mean_price = ('PRICE($)','mean'),
                                     state = ('DEALER LOCATION (STATE)','first')).reset_index()
            car_price['mean_price'] = round(car_price['mean_price'])

        elif select3 == 'SPECIFIC MODEL':
            with group3:
                select3_3 = st.selectbox('SELECT ONE',df['CAR NAME'].unique())
            with description3:
                select3_3_3 = st.selectbox('SELECT ONE',['OVERALL','NEW CARS','USED CARS'])
                st.write('DESCRIPTION')
                st.write("Visualize the distribution of specific car prices across the U.S. with this interactive map, highlighting average prices by state. The map includes Alaska and Hawaii for a comprehensive nationwide view.")
            
            if select3_3_3 == 'NEW CARS':
                specific_new3 = df[(df['STOCK TYPE'] == 'New') & (df['CAR NAME'] == select3_3)]
                car_price = specific_new3.groupby(['id']).agg(mean_price = ('PRICE($)','mean'),
                                     state = ('DEALER LOCATION (STATE)','first')).reset_index()
                car_price['mean_price'] = round(car_price['mean_price'])

            elif select3_3_3 == 'USED CARS':
                specific_used3 = df[(df['STOCK TYPE'] == 'Used') & (df['CAR NAME'] == select3_3)]
                car_price = specific_used3.groupby(['id']).agg(mean_price = ('PRICE($)','mean'),
                                     state = ('DEALER LOCATION (STATE)','first')).reset_index()
                car_price['mean_price'] = round(car_price['mean_price'])

            else:
               specific_overall3 = df[df['CAR NAME'] == select3_3]
               car_price = specific_overall3.groupby(['id']).agg(mean_price = ('PRICE($)','mean'),
                                     state = ('DEALER LOCATION (STATE)','first')).reset_index()
               car_price['mean_price'] = round(car_price['mean_price'])

            
        else:
               with description3:
                   st.write('DESCRIPTION')
                   st.write("Visualize the average car prices across U.S. states with an interactive map. This map highlights state-wise price variations, providing a clear comparison of mean prices.")
               car_price = df.groupby(['id']).agg(mean_price = ('PRICE($)','mean'),
                                     state = ('DEALER LOCATION (STATE)','first')).reset_index()


        st.write('-'*50)
        

        fig = px.choropleth_mapbox(
            car_price,
            geojson=us_states,
            locations='id',
            color='mean_price',
            hover_name='state', 
            hover_data={'mean_price': True}, 
            mapbox_style="carto-positron",
            center={"lat": 38, "lon": -96.5},  
            zoom=2,  
            opacity=0.5,
            title= "Car Price Distribution by State in USA"
        )

        fig.update_layout(
                mapbox_bounds={"west": -179, "east": -60, "south": 18, "north": 72},  # Adjusted bounds to include Alaska and Hawaii
                margin={"r": 0, "t": 50, "l": 0, "b": 0}  # Remove default margins
            )
        st.plotly_chart(fig, use_container_width=True)

        st.write('-'*50)





        group4,description4 = st.columns(2)
        with group4:
            select4 = st.selectbox("SELECT ANYONE",['OVERALL DEALER COUNT','NEW CARS','USED CARS','SPECIFIC MODEL'])
        
        if select4 == 'NEW CARS':
            with description4:
                st.write('DESCRIPTION')
                st.write("A choropleth map showing the concentration of car dealerships across U.S. states, highlighting the number of dealers in each state for new cars only.")
            df_new4 = df[df['STOCK TYPE'] == 'New']
            dealer_count4 = df_new4.groupby(['id']).agg(dealers_count = ('DEALER NAME','nunique'),
                                     state = ('DEALER LOCATION (STATE)','first')).reset_index()

        elif select4 == 'USED CARS':
            with description4:
                st.write('DESCRIPTION')
                st.write("A choropleth map showing the concentration of car dealerships across U.S. states, highlighting the number of dealers in each state for used cars only.")
            df_used4 = df[df['STOCK TYPE'] == 'Used']
            dealer_count4 = df_used4.groupby(['id']).agg(dealers_count = ('DEALER NAME','nunique'),
                                     state = ('DEALER LOCATION (STATE)','first')).reset_index()

        elif select4 == 'SPECIFIC MODEL':
            with group4:
                select4_4 = st.selectbox('SELECT ONE',df['CAR NAME'].unique())
            with description4:
                select4_4_4 = st.selectbox('SELECT ONE',['OVERALL','NEW CARS','USED CARS'])
                st.write('DESCRIPTION')
                st.write("The choropleth map highlights the distribution of car dealerships per state, with darker shades representing higher dealer counts for a specific car model.")
            
            if select4_4_4 == 'NEW CARS':
                specific_new4 = df[(df['STOCK TYPE'] == 'New') & (df['CAR NAME'] == select4_4)]
                dealer_count4 = specific_new4.groupby(['id']).agg(dealers_count = ('DEALER NAME','nunique'),
                                     state = ('DEALER LOCATION (STATE)','first')).reset_index()

            elif select4_4_4 == 'USED CARS':
                specific_used4 = df[(df['STOCK TYPE'] == 'Used') & (df['CAR NAME'] == select4_4)]
                dealer_count4 = specific_used4.groupby(['id']).agg(dealers_count = ('DEALER NAME','nunique'),
                                     state = ('DEALER LOCATION (STATE)','first')).reset_index()
            else:
               specific_overall4 = df[df['CAR NAME'] == select4_4]
               dealer_count4 = specific_overall4.groupby(['id']).agg(dealers_count = ('DEALER NAME','nunique'),
                                     state = ('DEALER LOCATION (STATE)','first')).reset_index()
            
            
        else:
               with description4:
                   st.write('DESCRIPTION')
                   st.write("Explore the geographic concentration of car dealerships across U.S. states with this choropleth map. The map highlights the number of unique dealers per state, providing insights into regional dealership density.")
               dealer_count4 = df.groupby(['id']).agg(dealers_count = ('DEALER NAME','nunique'),
                                     state = ('DEALER LOCATION (STATE)','first')).reset_index()

        st.write('-'*50)
        

        fig = px.choropleth_mapbox(
            dealer_count4,
                geojson=us_states,
                locations='id',
                color='dealers_count',
                hover_name='state', 
                hover_data={'dealers_count': True}, 
                mapbox_style="carto-positron",
                center={"lat": 38, "lon": -96.5},  
                zoom=2,  
                opacity=0.5,
                title= "Car Dealers count per state"
            )

        fig.update_layout(
                mapbox_bounds={"west": -179, "east": -60, "south": 18, "north": 72}, 
                margin={"r": 0, "t": 50, "l": 0, "b": 0}  
            )
        st.plotly_chart(fig, use_container_width=True)

        st.write('-'*50)


        

    selected_visualization = st.selectbox('CHOOSE TYPE OF VISUALIZATION',['BAR CHARTS','LINE CHARTS','HISTOGRAMS','PIE CHARTS','TREE MAP','SUNBRUST CHARTS','BUBBLE CHARTS','SCATTER CHARTS','BOX PLOTS','CARTOGRAPIC MAP','HEAT MAP'])

    if selected_visualization == 'BAR CHARTS':
        st.title('SHOWING ALL BAR CHARTS')
        col1,col2 = st.columns(2)
        with col1:
            st.warning('NOTE : If perticular bar is empty, data is not available for that bar!!')
        all_bar_charts(car_search_by_brand_df)
    elif selected_visualization == 'LINE CHARTS':
        st.title('SHOWING ALL LINE CHARTS')
        col1,col2 = st.columns(2)
        with col1:
            st.warning('NOTE : line chart may look distorted, if perticular data does not exits!!')
        all_line_charts(car_search_by_brand_df)
    elif selected_visualization == 'HISTOGRAMS':
        st.title('SHOWING ALL HISTOGRAMS')
        col1,col2 = st.columns(2)
        with col1:
            st.warning('NOTE : SOME DATA MAY BE LABELED AS 0 OR -1, MEANS DATA IS NOT COMPLETELY AVAILABLE!!')
        all_histograms(car_search_by_brand_df)
    elif selected_visualization == 'PIE CHARTS':
        st.title('SHOWING ALL PIE CAHRTS')
        all_piecharts(car_search_by_brand_df)
    
    elif selected_visualization == 'TREE MAP':
        st.title('SHOWING ALL TREE MAP')
        all_treemap(car_search_by_brand_df)
    
    elif selected_visualization == 'SUNBRUST CHARTS':
        st.title('SHOWING ALL SUNBRUST CHARTS')
        all_sunbrust(car_search_by_brand_df)
    elif selected_visualization == 'BUBBLE CHARTS':
        st.title("SHOWING ALL BUBBLE CHARTS")
        col1,col2 = st.columns(2)
        with col1:
            st.warning('NOTE : SOME RATINGS MAY BE LABELED AS 0 OR -1, MEANS DATA IS NOT COMPLETELY AVAILABLE!!')
        all_bubble(car_search_by_brand_df)
    elif selected_visualization == 'SCATTER CHARTS':
        col1,col2 = st.columns(2)
        with col1:
            st.warning('NOTE : SOME RATINGS MAY BE LABELED AS 0 OR -1, MEANS DATA IS NOT COMPLETELY AVAILABLE!!')
        st.title("SHOWING ALL SCATTER CHARTS")
        all_scatter(car_search_by_brand_df)
    elif selected_visualization == 'BOX PLOTS':
        st.title("SHOWING ALL BOX PLOTS")
        all_box(car_search_by_brand_df)
    elif selected_visualization == 'CARTOGRAPIC MAP':
        st.title('SHOWING ALL CATROGRAPHIC MAPS')
        col1,col2 = st.columns(2)
        with col1:
            st.warning('NOTE : DATA OF SOME STATE MAY NOT AVAILABLE!!')
        all_cartograpic(car_search_by_brand_df)
    else:
        st.title('HEAT MAP')
        cor_temp = car_search_by_brand_df.drop(columns=['BRAND',
                'CAR ID',
                'CAR NAME',
                'CAR TYPE',
                'DEALER LOCATION (CITY)',
                'DEALER LOCATION (STATE)',
                'DEALER NAME',
                'IMAGE',
                'MAKE ORIGIN',
                'MODEL/CLASS',
                'PARENT COMPANY',
                'PRICE RANGE',
                'STOCK TYPE','id'])

        corr_matrix = cor_temp.corr()

        fig = px.imshow(corr_matrix, 
                        text_auto=True, 
                        color_continuous_scale='Viridis', 
                        aspect="auto", 
                        title="Correlation Heatmap")

        st.plotly_chart(fig, use_container_width=True)

# Function to handle "Search by Category"
def search_by_category(final_df):
    visual_df = final_df.copy()
    st.title('Search by Category')

    col1,col2 = st.columns(2)
    with col1:
        brands = final_df['BRAND'].unique().tolist()
        brands = ['SELECT ALL'] + brands
        selected_subcategory = st.selectbox('SELECT BRANDS',brands)
    with col2:
        subcategory_options = st.selectbox('SHOW BY',['BEST RATING','LATEST MODEL!','OLDEST MODEL!','HIGHEST PRICE','LOWEST PRICE','ONLY NEW','ONLY OLD'],placeholder='SELECT ANY ONE')

    st.write('-'*50)

    if selected_subcategory == 'SELECT ALL':
        pass
    else:
        final_df = final_df[(final_df['BRAND'] == selected_subcategory)]

    if subcategory_options == 'BEST RATING':
        final_df = final_df[(final_df['RATING'] == final_df['RATING'].max())]
    elif subcategory_options == 'LATEST MODEL!':
        final_df = final_df[(final_df['MODEL'] == final_df['MODEL'].max())]
    elif subcategory_options == 'OLDEST MODEL!':
        final_df = final_df[(final_df['MODEL'] == final_df['MODEL'].min())]
    elif subcategory_options == 'HIGHEST PRICE':
        final_df = final_df[final_df['PRICE($)'] == final_df['PRICE($)'].max()]
    elif subcategory_options == 'LOWEST PRICE':
        final_df = final_df[final_df['PRICE($)'] == final_df['PRICE($)'].min()]
    elif subcategory_options == 'ONLY NEW':
        final_df = final_df[final_df['STOCK TYPE'] == 'New']
    else:
        final_df = final_df[final_df['STOCK TYPE'] == 'Used']
        
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Roboto:ital,wght@1,300&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

    # Create two responsive columns
    c1, c2 = st.columns(2)
    import requests
    def get_youtube_videos(car_name):
        api_key = 'AIzaSyCRmnPMnqiT1NMM7pTlZBeEp2ildwe5_rw'  
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={car_name}&type=video&key={api_key}'
        response = requests.get(url)
        data = response.json()
        
        if 'items' not in data:
            print("Error:", data)
            return []

        video_ids = [item['id']['videoId'] for item in data['items']]
        video_urls = [f"https://www.youtube.com/watch?v={video_id}" for video_id in video_ids]
        return video_urls
    
    fatch = final_df['CAR NAME'].values[0]
    videos = get_youtube_videos(f'{fatch} official video')
    video = videos[0]
    youtube_video_id = video.split('v=')[-1]
    # print(video)
    # print(youtube_video_id)

    with c1:
        autoplay_html = f"""
        <iframe width="100%" height="315" src="https://www.youtube.com/embed/{youtube_video_id}?autoplay=1&mute=0&loop=1&playlist={youtube_video_id}"
        title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        """
        st.markdown(autoplay_html, unsafe_allow_html=True)
        st.write(f'BEST OF {subcategory_options}')

    with c2:
        brand_taglines = {
            'Chevrolet': 'Find New Roads',
            'Toyota': "Let's Go Places",
            'Ford': 'Built Ford Tough',
            'Honda': 'The Power of Dreams',
            'Acura': 'Precision Crafted Performance',
            'Mazda': 'Feel Alive',
            'Nissan': 'Innovation that Excites',
            'Subaru': 'Love. It’s what makes a Subaru, a Subaru.',
            'BMW': 'The Ultimate Driving Machine',
            'MINI': 'Motoring Matters',
            'Pontiac': 'We Build Excitement',
            'Audi': 'Vorsprung durch Technik (Progress through Technology)',
            'Lexus': 'Experience Amazing',
            'Oldsmobile': 'Start Something',
            'Bentley': 'Be Extraordinary',
            'Jaguar': 'The Art of Performance',
            'Mitsubishi': 'Drive Your Ambition',
            'Jeep': 'Go Anywhere. Do Anything.',
            'Ferrari': 'We are the competition',
            'Mercedes-Benz': 'The Best or Nothing',
            'McLaren': 'Fearlessly Forward',
            'Porsche': 'There is No Substitute',
            'Rolls-Royce': 'Inspiration is the key',
            'Volvo': 'For Life',
            'Chrysler': 'Imported from Detroit',
            'AC': 'The Cobra, Simply the Best',
            'Alfa Romeo': 'La Meccanica delle Emozioni (The Mechanics of Emotion)',
            'Dodge': 'Domestic. Not Domesticated.',
            'FIAT': 'Driven by Passion',
            'Volkswagen': 'Das Auto (The Car)',
            'Maserati': 'Excellence through Passion',
            'Buick': 'Dream Big',
            'Triumph': 'For the Ride',
            'Cadillac': 'Dare Greatly',
            'Lamborghini': 'Expect the Unexpected',
            'INFINITI': 'Empower the Drive',
            'MG': 'The Classic Marque of Britain',
            'Saturn': 'A Different Kind of Car Company',
            'Lotus': 'For the Drivers',
            'Aston Martin': 'Power, Beauty, and Soul',
            'Saab': 'Born from Jets',
            'smart': 'Open Your Mind',
            'Plymouth': 'The Pride is Back',
            'Land Rover': 'Above and Beyond',
            'Austin-Healey': 'Built for Speed',
            'Tesla': 'Electric Cars, Solar & Clean Energy',
            'Packard': 'Ask the Man Who Owns One',
            'Excalibur': 'Elegant Motors for Exceptional People',
            'Mercury': 'New Doors Opened',
            'Kaiser': "America's First Postwar Car",
            'Sunbeam': 'Grace, Space, and Pace',
            'Datsun': 'Dare to be Different',
            'Panoz': 'Our Passion, Your Gain',
            'Suzuki': 'Way of Life!',
            'Nash': 'Give your Car a Lift',
            'Lincoln': 'American Luxury',
            'Aston': 'Power, Beauty, and Soul',
            'Scion': 'What Moves You',
            'Hyundai': 'New Thinking. New Possibilities.',
            'Kia': 'The Power to Surprise',
            'Alfa': 'La Meccanica delle Emozioni',
            'Rambler': 'Take it Easy!',
            'Bugatti': 'Ettore Bugatti',
            'Citroen': 'Inspired by You',
            'Bremen': 'A Touch of Class',
            'Austin': 'Grace, Space, Pace',
            'Polestar': 'Pure, Progressive Performance',
            'Lancia': 'The Power to Dream',
            'Delorean': 'Live the Dream',
            'Studebaker': 'First by far with a postwar car',
            'Avanti': 'The World’s Fastest Production Car',
            'DeTomaso': 'Style Never Dies',
            'Koenigsegg': 'The Spirit of Performance',
            'Eagle': 'The Premier Trail Vehicle',
            'GMC': 'We Are Professional Grade',
            'Genesis': 'Luxury Evolved',
            'Karma': 'Sustainable Luxury',
            'Lucid': 'The Future of Luxury',
            'RAM': 'Guts. Glory. Ram.',
            'VinFast': 'Boundless Together',
            'Rivian': 'Electric Adventure Vehicles',
            'Fisker': 'Revolutionary Clean Cars',
            'Isuzu': 'Go Your Own Way',
            'American Motors': 'Where quality is built in',
            'Geo': 'Get to know Geo',
            'Hummer': 'Like Nothing Else',
            'Am General': 'All American Freedom',
            'INEOS': 'Built on Purpose',
            'ALL CARS' : ''
        }

        company_name = f'ALL {final_df['CAR TYPE'].unique()[0]}' if selected_subcategory == 'SELECT ALL' else selected_subcategory
        tagline = brand_taglines[company_name] if selected_subcategory != 'SELECT ALL' else ''


        styled_html = f"""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 315px; width: 100%; background: #FFFFFF; border-radius: 15px; padding: 20px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); overflow: hidden; position: relative;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: radial-gradient(circle at 50% 50%, rgba(0, 0, 0, 0.05) 0%, rgba(0, 0, 0, 0) 70%); animation: pulse 5s infinite; z-index: 0;"></div>
            <div style="text-align: center; margin-bottom: 20px; animation: fadeIn 1.5s ease-in-out; z-index: 1; position: relative;">
                <h1 style="font-family: 'Montserrat', sans-serif; font-size: 3.5em; color: #333333; margin: 0; text-transform: uppercase; letter-spacing: 3px; border-bottom: 3px solid #4A90E2; padding-bottom: 10px; transition: color 0.3s ease;">
                    {company_name}
                </h1>
            </div>
            <div style="text-align: center; max-width: 80%; margin: 0 auto; animation: fadeIn 2s ease-in-out; z-index: 1; position: relative;">
                <p style="font-family: 'Roboto', sans-serif; font-size: 1.5em; color: #666666; margin: 0; font-style: italic; line-height: 1.6; transition: color 0.3s ease;">
                    "{tagline}"
                </p>
            </div>
        </div>

        <style>
        @keyframes fadeIn {{
            0% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}
        @keyframes pulse {{
            0% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
            100% {{ transform: scale(1); }}
        }}
        # div:hover h1 {{
        #     color: #4A90E2;
        # }}
        # div:hover p {{
        #     color: #333333;
        # }}
        # </style>
        """
        
        st.markdown(styled_html, unsafe_allow_html=True)
    

    

    st.write('\n'*10)
    st.header(f'SHOWING RESULTS BY {subcategory_options} !!')
    st.write('\n'*10)
    st.write('-'*50)

    
    if final_df.shape[0] == 0:
        st.subheader(f'no {subcategory_options} cars available!! search by other show by options!!')
    
    else:
        if 'current' not in st.session_state:
            st.session_state.current = 0

        if 'prev_df' not in st.session_state:
            st.session_state.prev_df = None

        if st.session_state.prev_df is None or not final_df.equals(st.session_state.prev_df):
            st.session_state.current = 0
            st.session_state.prev_df = final_df.copy()

        def showing_details(final_df):
            
            st.header(final_df['CAR NAME'].values[0])

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric('CAR STATUS', final_df['STOCK TYPE'].values[0])
                st.metric('MAKE ORIGIN', final_df['MAKE ORIGIN'].values[0])

            with col2:
                st.metric('PRICE(USD)', final_df['PRICE($)'].values[0])
                st.metric('MILEAGE', final_df['MILEAGE'].values[0])

            with col3:
                st.metric('MODEL YEAR', str(final_df['MODEL'].values[0]))
                st.metric('CAR TYPE', final_df['CAR TYPE'].values[0])

            st.metric('PARENT COMPANY', final_df['PARENT COMPANY'].values[0])

            st.markdown(f'<a href="{final_df["IMAGE"].values[0]}" target="_blank">Click here to open the original photo of this car (photo provided by dealer/owner)</a>', unsafe_allow_html=True)
            return final_df['CAR NAME'].values[0]

        previous, _, count, _, next = st.columns(5)

        total = final_df.shape[0]

        with previous:
                if st.button('PREVIOUS'):
                    if st.session_state.current > 0:
                        st.session_state.current -= 1
                    else:
                        st.session_state.current = total - 1 

        with next:
                if st.button('NEXT'):
                    if st.session_state.current < total - 1:
                        st.session_state.current += 1
                    else:
                        st.session_state.current = 0  

        with count:
            st.write(f'Showing {st.session_state.current + 1} out of {total}')

        st.write('*'*50)

        car = showing_details(final_df.iloc[st.session_state.current].to_frame().T)


    st.write('\n'*50)
    st.write('-'*50)

    import requests
    import random 

    def get_google_images(car_name):
        url = f"https://www.googleapis.com/customsearch/v1?q={car_name}&cx={'a1b7ef8be3781450e'}&searchType=image&key={'AIzaSyCRmnPMnqiT1NMM7pTlZBeEp2ildwe5_rw'}"
        response = requests.get(url)
        data = response.json()
        return [item['link'] for item in data.get('items', [])]

    photos = get_google_images(car)
    random.shuffle(photos)

    st.image(photos[0],f'{car}-image from google api')

    st.write('-'*50)
    
    st.header(f'ANALYSIS OF ALL {final_df['CAR TYPE'].unique()[0]}')


    def all_bar_charts(df):
        df.loc[df['STOCK TYPE'].str.contains('Certified'),'STOCK TYPE'] = 'Make Certified'

        st.write('-'*50)

        group1,description1 = st.columns(2)
        with group1:
            select1 = st.selectbox("SELECT ONE",['OVERALL COUNT','GROUPED CHART','NEW CARS','USED CARS','MAKE CERTIFIED'])
        
        with description1:
            st.write('DESCRIPTION')
            if select1 == 'OVERALL COUNT':
                st.write("Explore the diversity of car models across different brands. This bar chart showcases the unique car count for each brand, providing insights into brand variety.")
            elif select1 == 'GROUPED CHART':
                st.write("Visualize the comparison of multiple categories within each group. This grouped bar chart provides a clear side-by-side view of data points, making it easy to spot trends and differences.")
            elif select1 == 'USED CARS':
                st.write("Discover the distribution of used cars across different categories. This bar chart highlights the number of used cars, offering insights into the availability of pre-owned vehicles.")
            elif select1 == 'NEW CARS':
                st.write("Examine the distribution of new cars across various categories. This bar chart illustrates the count of new cars, providing a snapshot of the latest offerings.")
            else:
                st.write("Analyze the presence of certified cars across different categories. This bar chart displays the number of certified vehicles, giving an overview of certified options available.")
        
        df1 = df.groupby(['BRAND','STOCK TYPE'])['CAR NAME'].nunique().unstack(level=1).fillna(0)

        st.write('-'*50)

        if select1 == 'OVERALL COUNT':
            bar1 = df.groupby('BRAND')['CAR NAME'].nunique().reset_index()
            fig1 = px.bar(bar1,'BRAND','CAR NAME',labels={'CAR NAME' : 'CAR COUNT'})
            st.plotly_chart(fig1,use_container_width=True)

        elif select1 == 'GROUPED CHART':
            grouped = px.bar(df1,df1.index,df1.columns,barmode='group',text_auto=True,labels={'value' : 'CAR COUNT'})
            st.plotly_chart(grouped,use_container_width=True)

        elif select1 == 'NEW CARS':
            bar5 = df1[df1['New'] > 0]
            new = px.bar(bar5,bar5.index,'New',labels={'New' : 'NEW CARS COUNT'})
            st.plotly_chart(new,use_container_width=True)
        
        elif select1 == 'USED CARS':
            old = df1[df1['Used'] > 0]
            used = px.bar(old,old.index,'Used',labels={'Used' : 'USED CARS COUNT'})
            st.plotly_chart(used,use_container_width=True)

        else:
            certified = df1[df1['Make Certified'] > 0]
            certified_ = px.bar(certified,certified.index,'Make Certified',labels={'Make Certified' : 'Make Certified CARS COUNT'})
            st.plotly_chart(certified_,use_container_width=True)
        
        st.write('-'*50)

        group2,description2 = st.columns(2)
        ratings = df[df['RATING'] != -1]
        rating_ = ratings.groupby(['BRAND','STOCK TYPE'])['RATING'].mean().unstack(level=1).fillna(0)

        with group2:
            select2 = st.selectbox("SELECT ONE ",['OVERALL COUNT','GROUPED CHART','NEW CARS','USED CARS','MAKE CERTIFIED'])
        
        with description2:
            st.write('DESCRIPTION')
            if select1 == 'OVERALL COUNT':
                st.write("View the average ratings for each brand. This bar chart provides an overview of brand performance based on user ratings, highlighting overall satisfaction levels.")
            elif select1 == 'GROUPED CHART':
                st.write("Compare ratings across different categories within each brand. This grouped bar chart allows for an in-depth analysis of rating trends across multiple aspects.")
            elif select1 == 'USED CARS':
                st.write("Explore the ratings of used cars across various categories. This bar chart highlights how pre-owned vehicles are rated, providing insights into their performance.")
            elif select1 == 'NEW CARS':
                st.write("Examine the ratings of new cars across different categories. This bar chart showcases the performance of newly available vehicles, reflecting their user ratings.")
            else:
                st.write("Analyze the ratings of certified cars across various categories. This bar chart displays how certified vehicles are rated, offering insights into their quality and performance.")
        
        df1 = df.groupby(['BRAND','STOCK TYPE'])['CAR NAME'].nunique().unstack(level=1).fillna(0)

        st.write('-'*50)

        if select2 == 'OVERALL COUNT':
            overall = ratings.groupby('BRAND')['RATING'].mean()
            fig2 = px.bar(overall,overall.index,overall.values,text_auto=True,labels={'y' : 'RATING'})
            st.plotly_chart(fig2,use_container_width=True)

        elif select2 == 'GROUPED CHART':
            grouped = px.bar(rating_,rating_.index,rating_.columns,barmode='group',text_auto=True,labels={'value' : 'RATING'})
            st.plotly_chart(grouped,use_container_width=True)

        elif select2 == 'NEW CARS':
            r3 = rating_[rating_['New'] > 0]
            new = px.bar(r3,r3.index,'New',text_auto=True,labels={'New' : 'NEW CARS RATING'})
            st.plotly_chart(new,use_container_width=True)
        
        elif select2 == 'USED CARS':
            r2 = rating_[rating_['Used'] > 0]
            used = px.bar(r2,r2.index,'Used',text_auto=True,labels={'Used' : 'USED CARS RATING'})
            st.plotly_chart(used,use_container_width=True)

        else:
            r4 = rating_[rating_['Make Certified'] > 0]
            certified_ = px.bar(r4,r4.index,'Make Certified',text_auto=True,labels={'Make Certified' : 'MAKE CERTIFIED CARS RATING'})
            st.plotly_chart(certified_,use_container_width=True)
        
        st.write('-'*50)
    
        group3,description3 = st.columns(2)
        with group3:
            select3 = st.selectbox('SELECT ONE',['TOP DEALER OF EACH BRAND','NUMBER OF DEALER FOR EACH BRAND'])
        with description3:
            st.write('DESCRIPTION')
            if select3 == 'TOP DEALER OF EACH BRAND':
                st.write("Identify the top dealer for each brand based on car count. This bar chart highlights the dealer with the highest number of cars for each brand, showcasing top performers in the market.")
            else:
                st.write("Visualize brands with multiple dealers. This bar chart displays brands that have more than one dealer, excluding those with only a single dealer, and provides insights into brand distribution across the market.")
        st.write('-'*50)
        
        if select3 == 'TOP DEALER OF EACH BRAND':
            dealers = df.groupby(['DEALER NAME','BRAND'])['CAR NAME'].count().reset_index()
            dealers1 = dealers.groupby('BRAND')['CAR NAME'].max().reset_index().merge(dealers,how='inner',on=['BRAND','CAR NAME'])
            dealers1 = dealers1.drop_duplicates(['BRAND','CAR NAME'],keep='first')
            dealers1 = dealers1[dealers1['CAR NAME'] > 1]
            topdealer = px.bar(dealers1,'DEALER NAME','CAR NAME',text_auto=True,labels={'CAR NAME' : 'DEALER COUNT'})
            st.plotly_chart(topdealer,use_container_width=True)
        
        else:
            dealers2  = df.groupby('BRAND')['DEALER NAME'].nunique().reset_index()
            dealers2 = dealers2[dealers2['DEALER NAME'] > 1]
            alldealer = px.bar(dealers2,'BRAND','DEALER NAME',text_auto=True,labels={'DEALER NAME' : 'DEALER COUNT'})
            st.plotly_chart(alldealer,use_container_width=True)

        st.write('-'*50)

        group4,description4 = st.columns(2)
        with group4:
            select4 = st.selectbox('SELECT ONE',['MAKE ORIGIN WISE PRICE','MAKE ORIGIN WISE RATING','NUMBER OF BRANDS FROM DIFFERENT COUNTRY'])
        with description4:
            st.write('DESCRIPTION')
            if select4 == 'MAKE ORIGIN WISE PRICE':
                st.write("Compare average prices by car origin. This bar chart displays the average price of new cars based on their make origin, offering insights into pricing trends across different regions.")
            elif select4 == 'MAKE ORIGIN WISE RATING':
                st.write("Examine average ratings by car origin. This bar chart presents the average ratings of new cars based on their make origin, highlighting performance trends across different regions.")
            else:
                st.write("Explore the number of brands from each car origin. This bar chart shows the count of unique brands for each make origin, providing insights into brand diversity across regions.")
        
        st.write('-'*50)
        
        if select4 == 'MAKE ORIGIN WISE PRICE':
            make_origin = df[df['STOCK TYPE'] == 'New']
            avg_price = make_origin.groupby('MAKE ORIGIN')['PRICE($)'].mean()
            price_chart = px.bar(avg_price,avg_price.index,avg_price.values,text_auto=True,labels={'y' : 'AVERAGE PRICE'})
            st.plotly_chart(price_chart,use_container_width=True)
        
        elif select4 == 'MAKE ORIGIN WISE RATING':
            make_rating = df[(df['STOCK TYPE'] == 'New') & (df['RATING'] != -1)]
            avg_rating = make_rating.groupby('MAKE ORIGIN')['RATING'].mean()
            rating_chart = px.bar(avg_rating,avg_rating.index,avg_rating.values,text_auto=True,labels={'y' : 'AVERAGE RATING'})
            st.plotly_chart(rating_chart,use_container_width=True)
        
        else:
            make_count = df.groupby(['MAKE ORIGIN'])['BRAND'].nunique()
            brand_count = px.bar(make_count,make_count.index,make_count.values,text_auto=True,labels={'y' : 'MAKE COUNT'})
            st.plotly_chart(brand_count,use_container_width=True)
        
        st.write('-'*50)

    def all_line_charts(df):

        df.loc[df['STOCK TYPE'].str.contains('Certified'),'STOCK TYPE'] = 'Make Certified'

        st.write('-'*50)
        group1,description1 = st.columns(2)
        with group1:
            select1 = st.selectbox('SELECT ONE',['OVERALL','NEW','USED','MAKE CERTIFIED'])
        with description1:
            st.write('DESCRIPTION')
            if select1 == 'OVERALL':
                st.write("Visualize overall price trends across different stock types with this line chart. It displays average prices for each brand, providing insights into pricing patterns over time.")

            elif select1 == 'NEW':
                st.write("Analyze pricing trends for new cars with this line chart. It highlights variations in average prices for each brand specifically for new stock types")
            
            elif select1 == 'USED':
                st.write("Examine pricing trends for used cars with this line chart. It shows average prices for each brand specifically for used stock types.")
            
            else:
                st.write("Examine price trends for certified cars with this line chart. It displays variations in average prices for each brand, focusing on certified stock types over time.")
        st.write('-'*50)

        line1 = df.groupby(['BRAND','STOCK TYPE'])['PRICE($)'].mean().unstack(level=1).fillna(-1)

        if select1 == 'OVERALL':
            overall = px.line(line1,line1.index,line1.columns,labels={'value':'PRICE'})
            st.plotly_chart(overall,use_container_width=True)

        elif select1 == 'NEW':
            new = line1[line1['New'] > 0]
            new = px.line(new,new.index,'New',labels={'New':'PRICE'})
            st.plotly_chart(new,use_container_width=True)
        
        elif select1 == 'USED':
            used = line1[line1['Used'] > 0]
            used = px.line(used,used.index,'Used',labels={'Used':'PRICE'})
            st.plotly_chart(used,use_container_width=True)

        elif select1 == 'MAKE CERTIFIED':
            certified = line1[line1['Make Certified'] > 0]
            certified = px.line(certified,certified.index,'Make Certified',labels={'Make Certified':'PRICE'})
            st.plotly_chart(certified,use_container_width=True)
        
        st.write('-'*50)

        group2,description2 = st.columns(2)
        with group2:
            select2 = st.selectbox('SELECT ONE',['OVERALL','NEW','USED','CERTIFIED'])
        with description2:
            st.write('DESCRIPTION')
            if select2 == 'OVERALL':
                st.write("View overall rating trends across different stock types with this line chart. It showcases the average ratings for each brand.")
            elif select2 == 'NEW':
                st.write("Track rating trends for new cars with this line chart. It highlights the average ratings for each brand.")
            elif select2 == 'USED':
                st.write("Analyze rating trends for used cars with this line chart. It displays the average ratings for each brand.")
            else:
                st.write("Explore rating trends for certified cars with this line chart. It showcases the average ratings for each brand.")
        st.write('-'*50)

        df = df[df['RATING'] != -1]
        line2 = df.groupby(['BRAND','STOCK TYPE'])['RATING'].mean().unstack(level=1).fillna(-1)

        if select2 == 'OVERALL':
            overall = px.line(line2,line2.index,line2.columns,labels={'value':'PRICE'})
            st.plotly_chart(overall,use_container_width=True)
        
        elif select2 == 'NEW':
            new = line2[line2['New'] > 0]
            new = px.line(new,new.index,'New',labels={'New':'PRICE'})
            st.plotly_chart(new,use_container_width=True)

        elif select2 == 'USED':
            used = line2[line2['Used'] > 0]
            used = px.line(used,used.index,'Used',labels={'Used':'PRICE'})
            st.plotly_chart(used,use_container_width=True)

        elif select2 == 'CERTIFIED':
            certified = line2[line2['Make Certified'] > 0]
            certified = px.line(certified,certified.index,'Make Certified',labels={'Make Certified':'PRICE'})
            st.plotly_chart(certified,use_container_width=True)

        st.write('-'*50)

        group3,description3 = st.columns(2)
        with group3:
            select3 = st.selectbox('SELECT ONE',['MILEAGE OF USED CARS'])
        with description3:
            st.write('DESCRIPTION')
            st.write("Discover the average mileage of used cars with this line chart. It highlights the mileage trends for each brand, offering insights into the longevity and usage of pre-owned vehicles.")
        
        st.write('-'*50)

        if select3 == 'MILEAGE OF USED CARS':
            old = df[df['STOCK TYPE'] == 'Used']
            mileage = old.groupby('BRAND')['MILEAGE'].mean()
            mileage = px.line(mileage,mileage.index,mileage.values,labels={'y':'PRICE'})
            st.plotly_chart(mileage,use_container_width=True)

        st.write('-'*50)

        
    def all_histograms(df):
        df.loc[df['STOCK TYPE'].str.contains('Certified'),'STOCK TYPE'] = 'Make Certified'

        st.write('-'*50)
        st.write('DESCRIPTION')
        st.write("Explore the average mileage of used car brands through this histogram, categorized by stock type. Easily compare how mileage varies across different brands.")
        mileage = df[df['STOCK TYPE'] != 'New']
        mileage = mileage.groupby(['BRAND','STOCK TYPE'])['MILEAGE'].mean().reset_index()
        fig1 = px.histogram(mileage,'MILEAGE',color='STOCK TYPE',text_auto=True,title="Average Mileage Distribution by Stock Type")
        st.plotly_chart(fig1,use_container_width=True)

        st.write('-'*50)
        st.write('DESCRIPTION')
        st.write("Analyze the distribution of car ages for used/make-certified vehicles with this histogram, grouped by stock type. See how age varies across different categories, New cars are not included.")
        age = df[df['STOCK TYPE'] != 'New']
        fig2 = px.histogram(age,'AGE OF CAR',color='STOCK TYPE',text_auto=True,title='Car Age Distribution for Used/Make-Certified Vehicles"')
        st.plotly_chart(fig2,use_container_width=True)

        st.write('-'*50)
        st.write('DESCRIPTION')
        st.write("Examine car ratings in this histogram, filtered for valid ratings and categorized by stock type. The data is grouped into five bins for a clearer comparison.")
        df = df[df['RATING'] != -1]
        fig3 = px.histogram(df,'RATING',color='STOCK TYPE',text_auto=True,nbins=5,title="Car Ratings by Stock Type with Binned Distribution")
        st.plotly_chart(fig3,use_container_width=True)
        st.write('-'*50)

    def all_piecharts(df):
        
        st.write('-'*50)
        group1,description1 = st.columns(2)
        with description1:
            for i in range(3):
                st.write('|')
            st.write('| DESCRIPTION')
            st.write("| This pie chart displays the top car brands in the dataset, showing their share of the total count. The chart combines percentage and label information for a clear overview.")
            for i in range(3):
                st.write('|')


        with group1:
            pie1 = df['BRAND'].value_counts().reset_index().head(10)
            fig = px.pie(pie1, names='BRAND', values='count',title='Top Car Brands by Count')
            fig.update_traces(textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
        st.write('-'*50)


        group2,description2 = st.columns(2)
        with description2:
            for i in range(3):
                st.write('|')
            st.write('| DESCRIPTION')
            st.write("| This pie chart illustrates the distribution of cars across different stock types, including certified vehicles, showing each category's share of the total inventory.")
            for i in range(3):
                st.write('|')


        with group2:
            df.loc[df['STOCK TYPE'].str.contains('Certified'),'STOCK TYPE'] = 'Make Certified'
            pie4 = df.groupby('STOCK TYPE')['CAR NAME'].count().reset_index(name='CAR COUNT')
            fig1 = px.pie(pie4,names='STOCK TYPE',values='CAR COUNT',title="Car Distribution by Stock Type")
            fig1.update_traces(textinfo='percent+label')
            st.plotly_chart(fig1,use_container_width=True)

        st.write('-'*50)

        group3,description3 = st.columns(2)
        with description3:
            for i in range(3):
                st.write('|')
            st.write('| DESCRIPTION')
            st.write("| This pie chart showcases the top car brands by count, segmented by stock type. It provides a clear view of each brand's inventory distribution, combining percentage and label information.")
            for i in range(3):
                st.write('|')


        with group3:
            pie2 = df.groupby(['BRAND','STOCK TYPE'])['CAR NAME'].count().reset_index(name='CAR COUNT')
            pie2 = pie2.sort_values('CAR COUNT',ascending=False).head(20)
            fig3 = px.pie(pie2,names='BRAND',values='CAR COUNT',color='STOCK TYPE',title='Top Car Brands by Stock Type')
            fig3.update_traces(textinfo='percent+label')
            st.plotly_chart(fig3,use_container_width=True)
        st.write('-'*50)

        group6,description6 = st.columns(2)
        with description6:
            for i in range(3):
                st.write('|')
            st.write('| DESCRIPTION')
            st.write("| This pie chart highlights the distribution of cars based on their origin, differentiating between USA-made and foreign vehicles. The chart combines percentage and label information for clarity.")
            for i in range(3):
                st.write('|')


        with group6:
            df.loc[df['MAKE ORIGIN'] != 'USA','MAKE ORIGIN'] = 'Foreign'
            pie6 = df['MAKE ORIGIN'].value_counts().reset_index()
            fig6 = px.pie(pie6,names='MAKE ORIGIN',values='count',title="Car Distribution by Make Origin")
            fig6.update_traces(textinfo='percent+label')
            st.plotly_chart(fig6,use_container_width=True)
        st.write('-'*50)

        group7,description7 = st.columns(2)
        with description7:
            for i in range(3):
                st.write('|')
            st.write('| DESCRIPTION')
            st.write("| This pie chart displays the top car brands by count, categorized by their origin (USA vs. Foreign). It provides a clear comparison of the leading brands based on their make origin, with percentage and label details.")
            for i in range(3):
                st.write('|')


        with group7:
            brandwise = df.groupby(['MAKE ORIGIN','BRAND'])['CAR NAME'].count().reset_index(name='CAR COUNT')
            brandwise = brandwise.sort_values('CAR COUNT',ascending=False).head(10)
            fig = px.pie(brandwise,names='BRAND',values='CAR COUNT',color='MAKE ORIGIN',title="Top Car Brands by Make Origin")
            fig.update_traces(textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
        st.write('-'*50)


        st.write('| DESCRIPTION')
        st.write("| This pie chart highlights the top states with the highest car dealer inventory, showing each state's share of the total count. The chart combines percentage and label information for clarity.")
        
        pie5 = df.groupby('DEALER LOCATION (STATE)')['CAR NAME'].count().reset_index(name='CAR COUNT')
        pie5 = pie5.sort_values('CAR COUNT',ascending=False).head(20)
        fig5 = px.pie(pie5,names='DEALER LOCATION (STATE)',values='CAR COUNT',title="Top States by Car Dealer Inventory")
        fig5.update_traces(textinfo='percent+label')
        st.plotly_chart(fig5,use_container_width=True)

        st.write('-'*50)

        st.write('| DESCRIPTION')
        st.write("| This pie chart showcases the top car dealers based on inventory size, highlighting each dealer's contribution to the total count with percentage and label details.")

        pie3 = df.groupby('DEALER NAME')['CAR NAME'].count().reset_index(name='CAR COUNT')
        pie3 = pie3.sort_values('CAR COUNT',ascending=False).head(10)
        fig4 = px.pie(pie3,names='DEALER NAME',values='CAR COUNT',title="Top Car Dealers by Inventory")
        fig4.update_traces(textinfo='percent+label')
        st.plotly_chart(fig4,use_container_width=True)
        
        st.write('-'*50)
            

    def all_treemap(df):
        
        st.write('-'*50)
        group1,description1 = st.columns(2)
        with group1:
            select1 = st.selectbox('SELECT ONE',['PARENT COMPANY --> BRAND --> UNIQUE CAR COUNTS','PARENT COMPANY --> BRAND --> STOCK TYPE --> UNIQUE CAR COUNTS'])
        with description1:
            st.write('DESCRIPTION')
            if select1 == 'PARENT COMPANY --> BRAND --> UNIQUE CAR COUNTS':
                st.write("This treemap visualizes the diversity of car models under each parent company, breaking down the unique model count by brand for a comprehensive overview.")
            else:
                st.write("Discover the variety of unique car models available across different stock types, organized by parent company and brand in this detailed treemap.")
        st.write('-'*50)
        
        if select1 == 'PARENT COMPANY --> BRAND --> UNIQUE CAR COUNTS':
            tree1 = df.groupby(['PARENT COMPANY','BRAND'])['CAR NAME'].nunique().reset_index(name='CAR COUNT')
            fig = px.treemap(tree1,path=[px.Constant('CARS'),'PARENT COMPANY','BRAND'],values='CAR COUNT',title="Unique Car Models by Parent Company and Brand")
            st.plotly_chart(fig,use_container_width=True)
        
        else:
            tree2 = df.groupby(['PARENT COMPANY','BRAND','STOCK TYPE'])['CAR NAME'].nunique().reset_index(name='CAR COUNT')
            fig = px.treemap(tree2,path=[px.Constant('CARS'),'PARENT COMPANY','BRAND','STOCK TYPE'],values='CAR COUNT',title= "Unique Car Models by Parent Company, Brand, and Stock Type")
            st.plotly_chart(fig,use_container_width=True)
        
        st.write('-'*50)
        group2,description2 = st.columns(2)
        with group2:
            select2 = st.selectbox('SELECT ONE',['DEALERS WITH MOST NUMBER OF CARS','TOP DEALER OF EACH BRAND'])
        with description2:
            st.write('DESCRIPTION')
            if select2 == 'DEALERS WITH MOST NUMBER OF CARS':
                st.write("Visualize the top car dealers with the most inventory using this treemap. The chart breaks down the count by dealer and brand for a clear comparison.")
            else:
                st.write( "Explore the top dealer for each car brand using this treemap. The chart highlights which dealers have the most inventory for each brand, providing a clear brand-to-dealer relationship.")
        st.write('-'*50)


        if select2 == 'DEALERS WITH MOST NUMBER OF CARS':
            tree3 = df.groupby(['DEALER NAME','BRAND'])['CAR NAME'].count().reset_index(name='CAR COUNT')
            tree3 = tree3.sort_values('CAR COUNT',ascending=False).head(20)
            fig2 = px.treemap(tree3,path=[px.Constant('CARS'),'DEALER NAME','BRAND'],values='CAR COUNT',title= "Top Dealers by Car Inventory")
            st.plotly_chart(fig2,use_container_width=True)

        else:
            dealers = df.groupby(['DEALER NAME','BRAND'])['CAR NAME'].count().reset_index()

            dealers1 = dealers.groupby('BRAND')['CAR NAME'].max().reset_index().merge(dealers,how='inner',on=['BRAND','CAR NAME'])

            dealers1 = dealers1.drop_duplicates(['BRAND','CAR NAME'],keep='first')

            fig2 = px.treemap(dealers1,path=[px.Constant('CARS'),'BRAND','DEALER NAME'],values='CAR NAME',title= "Top Dealers by Brand Inventory")
            st.plotly_chart(fig2,use_container_width=True)
        st.write('-'*50)


    def all_sunbrust(df):
        st.write('-'*50)
        st.write('DESCRIPTION')
        st.write("This sunburst chart provides a visual breakdown of car brands within their respective parent companies, offering an intuitive way to explore brand ownership.")
        fig = px.sunburst(df,path=['PARENT COMPANY','BRAND'],title='Hierarchical Overview of Parent Companies and Brands')
        st.plotly_chart(fig,use_container_width=True)
        st.write('-'*50)

        st.write('DESCRIPTION')
        st.write( "Explore the hierarchical relationship between car brands and their models/classes with this sunburst chart, revealing how different models are distributed under each brand.")
        fig2 = px.sunburst(df,path=['BRAND','MODEL/CLASS'],title="Brand and Model/Class Distribution")
        st.plotly_chart(fig2,use_container_width=True)
        st.write('-'*50)

        st.write('DESCRIPTION')
        st.write("Visualize the distribution of car models and their stock types within each brand using this sunburst chart. It highlights the hierarchical structure of brands, stock types, and models/classes.")
        fig3 = px.sunburst(df,path=['BRAND','STOCK TYPE','MODEL/CLASS'],title= "Brand, Stock Type, and Model/Class Breakdown")
        st.plotly_chart(fig3,use_container_width=True)

        st.write('-'*50)
        st.write('DESCRIPTION')
        st.write( "This sunburst chart visualizes the relationship between top dealers and car models/classes. It highlights which models are available at each leading dealer, providing a detailed view of dealer inventory.")
        dealers = df.groupby(['DEALER NAME','BRAND'])['CAR NAME'].count().reset_index()
        dealers1 = dealers.groupby('BRAND')['CAR NAME'].max().reset_index().merge(dealers,how='inner',on=['BRAND','CAR NAME'])
        dealers1 = dealers1.drop_duplicates(['BRAND','CAR NAME'],keep='first')
        sunbrust2 = df[df['DEALER NAME'].apply(lambda x : x in dealers1['DEALER NAME'].tolist())]
        fig4 = px.sunburst(sunbrust2,path=['DEALER NAME','MODEL/CLASS'],title='Dealer and Model/Class Distribution')
        st.plotly_chart(fig4,use_container_width=True)
        st.write('-'*50)

    def all_box(df):
        st.write('-'*50)
        group1,description1 = st.columns(2)
        with group1:
            select1 = st.selectbox('SELECT ONE',['OVERALL PRICE DISTRIBUTION','PRICE DISTIBUTION PER BRAND'])
        with description1:
            st.write('DESCRIPTION')
            if select1 == 'OVERALL PRICE DISTRIBUTION':
                st.write( "Analyze the distribution of car prices with this box plot, showcasing the range, median, and variability in prices across the dataset.")
            else:
                st.write( "Compare car prices across different brands using this box plot, which highlights the range and distribution of prices for each brand.")
        st.write('-'*50)
        
        if select1 == 'OVERALL PRICE DISTRIBUTION':
            fig1 = px.box(df,'PRICE($)',title="Overall Price Distribution")
            st.plotly_chart(fig1,use_container_width=True)
        else:
            fig2 = px.box(df,'BRAND','PRICE($)',title= "Price Distribution by Brand")
            st.plotly_chart(fig2,use_container_width=True)
        st.write('-'*50)
        
        group2,description2 = st.columns(2)
        with group2:
            select2 = st.selectbox('SELECT ONE',['STOCK TYPE WISE PRICE DISTRIBUTION : OVERALL','STOCK TYPE WISE PRICE DISTRIBUTION : FOR EACH BRAND'])
        with description2:
            st.write('DESCRIPTION')
            if select2 == 'STOCK TYPE WISE PRICE DISTRIBUTION : OVERALL':
                st.write("Examine how car prices vary across different stock types with this box plot, providing insights into the overall pricing trends for new and used vehicles.")
            else:
                st.write( "Explore car price variations across brands, differentiated by stock type, with this box plot. It provides a detailed view of how prices differ for new and used vehicles within each brand.")
        st.write('-'*50)

        df.loc[df['STOCK TYPE'].str.contains('Certified'),'STOCK TYPE'] = 'Make Certified'

        if select2 == 'STOCK TYPE WISE PRICE DISTRIBUTION : OVERALL':
            fig1 = px.box(df,'STOCK TYPE','PRICE($)',title='Price Distribution by Stock Type')
            st.plotly_chart(fig1,use_container_width=True)
        else:
            fig1 = px.box(df,'BRAND','PRICE($)',color='STOCK TYPE',title='Price Distribution by Brand and Stock Type')
            st.plotly_chart(fig1,use_container_width=True)
        st.write('-'*50)

        group3,description3 = st.columns(2)
        with group3:
            select3 = st.selectbox('SELECT ONE',['MILEAGE DISTRIBUTION : OVERALL','MILEAGE DISTRIBUTION : FOR EACH BRAND'])
        with description3:
            st.write('DESCRIPTION')
            if select3 == 'MILEAGE DISTRIBUTION : OVERALL':
                st.write("View the distribution of car mileage across the dataset with this box plot, highlighting the range, median, and variability in mileage values.")
            else:
                st.write( "Analyze how mileage varies across different car brands with this box plot, revealing the range and central tendencies of mileage for each brand.")
        st.write('-'*50)

        if select3 == 'MILEAGE DISTRIBUTION : OVERALL':
            fig1 = px.box(df,'MILEAGE',title='Overall Mileage Distribution')
            st.plotly_chart(fig1,use_container_width=True)
        else:
            fig1 = px.box(df,'BRAND','MILEAGE',title="Mileage Distribution by Brand")
            st.plotly_chart(fig1,use_container_width=True)
        st.write('-'*50)

        group4,description4 = st.columns(2)
        with group4:
            select4 = st.selectbox('SELECT ONE',['RATING DISTRIBUTION : OVERALL','RATING DESTRIBUTION : FOR EACH BRAND'])
        with description4:
            st.write('DESCRIPTION')
            if select4 == 'RATING DISTRIBUTION : OVERALL':
                st.write()
            else:
                st.write()

        if select4 == 'RATING DISTRIBUTION : OVERALL':
            fig1 = px.box(df,'RATING')
            st.plotly_chart(fig1,use_container_width=True)
        else:
            ratings = df[df['RATING'] != -1] 
            fig1 = px.box(ratings,'BRAND','RATING')
            st.plotly_chart(fig1,use_container_width=True)


    def all_cartograpic(df):
        pass


    selected_visualization = st.selectbox('CHOOSE TYPE OF VISUALIZATION',['BAR CHARTS','LINE CHARTS','HISTOGRAMS','PIE CHARTS','TREE MAP','SUNBRUST CHARTS','BOX PLOTS','CARTOGRAPIC MAP','HEAT MAP'])

    if selected_visualization == 'BAR CHARTS':
        st.title('SHOWING ALL BAR CHARTS')
        col1,col2 = st.columns(2)
        with col1:
            st.warning('NOTE : If perticular bar is empty, data is not available for that bar!!')
        all_bar_charts(visual_df)
    elif selected_visualization == 'LINE CHARTS':
        st.title('SHOWING ALL LINE CHARTS')
        col1,col2 = st.columns(2)
        with col1:
            st.warning('NOTE : line chart may look distorted, if perticular data does not exits!!')
        all_line_charts(visual_df)
    elif selected_visualization == 'HISTOGRAMS':
        st.title('SHOWING ALL HISTOGRAMS')
        col1,col2 = st.columns(2)
        with col1:
            st.warning('NOTE : SOME DATA MAY BE LABELED AS 0 OR -1, MEANS DATA IS NOT COMPLETELY AVAILABLE!!')
        all_histograms(visual_df)
    elif selected_visualization == 'PIE CHARTS':
        st.title('SHOWING ALL PIE CAHRTS')
        all_piecharts(visual_df)
    
    elif selected_visualization == 'TREE MAP':
        st.title('SHOWING ALL TREE MAP')
        all_treemap(visual_df)
    
    elif selected_visualization == 'SUNBRUST CHARTS':
        st.title('SHOWING ALL SUNBRUST CHARTS')
        all_sunbrust(visual_df)
    elif selected_visualization == 'BOX PLOTS':
        st.title("SHOWING ALL BOX PLOTS")
        all_box(visual_df)
    elif selected_visualization == 'CARTOGRAPIC MAP':
        st.title('SHOWING ALL CATROGRAPHIC MAPS')
        col1,col2 = st.columns(2)
        with col1:
            st.warning('NOTE : DATA OF SOME STATE MAY NOT AVAILABLE!!')
        all_cartograpic(visual_df)
    else:
        st.title('HEAT MAP')
        cor_temp = visual_df.drop(columns=['BRAND',
                'CAR ID',
                'CAR NAME',
                'CAR TYPE',
                'DEALER LOCATION (CITY)',
                'DEALER LOCATION (STATE)',
                'DEALER NAME',
                'IMAGE',
                'MAKE ORIGIN',
                'MODEL/CLASS',
                'PARENT COMPANY',
                'PRICE RANGE',
                'STOCK TYPE','id'])

        corr_matrix = cor_temp.corr()

        fig = px.imshow(corr_matrix, 
                        text_auto=True, 
                        color_continuous_scale='Viridis', 
                        aspect="auto", 
                        title="Correlation Heatmap")

        st.plotly_chart(fig, use_container_width=True)



def EDA(df):
    st.title('CRISP OF EDA')
    st.markdown(f'<a href="{'https://colab.research.google.com/drive/1aK0VaLN8RasvfZ3qn8jS22WpO1ohSz-L?usp=sharing'}" target="_blank">Click here to see full EDA file</a>', unsafe_allow_html=True)
    st.header('Insights')
    st.write(
        """
        - **Ford Motor Company** is the parent company with the most cars in the dataset, accounting for 16.6% of the total. It is followed closely by **General Motors** (16%), **Daimler AG** (12.4%), and **Toyota** (10%).
        - Companies like **Ineos Automotive Ltd**, **Studebaker Corporation**, **Excalibur Automobile Company**, and **Koenigsegg Automotive AB** have the fewest cars in the dataset, with only one car each. This is followed by **Isuzu Motors Limited**, **De Tomaso Automobili**, **DeLorean Motor Company**, and **Bremen**, each with two cars.
        """
    )

    parent = df['PARENT COMPANY'].value_counts()
    fig = px.pie(parent,names=parent.index,values=parent.values)
    fig.update_traces(textinfo='label+percent')
    st.plotly_chart(fig,use_container_width=True)

    st.write(
    """
    - **MAKE ORIGIN** from the **United States** has the highest number of cars in the dataset, with approximately 100,000 cars (39.5%), followed by **Japan** with around 76,000 cars (28.7%) and **Germany** with 65,000 cars (24.5%).
    - **France** has the fewest cars in the dataset, with only 11 cars, followed by **Vietnam** with 15 cars and **India** with 501 cars.
    """
    )
    makes = df['MAKE ORIGIN'].value_counts()
    fig = px.pie(makes,names=makes.index,values=makes.values)
    fig.update_traces(textinfo = 'label+percent+value')
    st.plotly_chart(fig,use_container_width=True)
    st.write(
    """
    - **Ford** has the highest number of cars in the dataset, with 40,000 cars (16%), followed by **Mercedes-Benz** with 30,000 cars (12.1%), **Chevrolet** with 26,000 cars (10.5%), and **Toyota** with 23,000 cars (9.2%).
    - Companies like **INEOS**, **Kaiser**, **Nash**, **Rambler**, **Citroën**, **Austin**, **Lancia**, **Studebaker**, **Koenigsegg**, **Eagle**, **Excalibur**, and **Geo** each have only one car in the dataset. Most of these cars are from companies that are no longer in operation due to their age.
    """
    )
    brands = df['BRAND'].value_counts()
    pie = brands.head(20)
    fig = px.pie(pie,names=pie.index,values=pie.values)
    fig.update_traces(textinfo='label+value')
    st.plotly_chart(fig,use_container_width=True)

    fig = px.pie(pie,names=pie.index,values=pie.values,hole=0.4)
    fig.update_traces(textinfo='label+percent')
    st.plotly_chart(fig,use_container_width=True)
    st.write(
    """
    - Most car models in the dataset are from the years **2020 to 2024**, totaling around 1.95k cars, followed by models from **2015 to 2019** with 38k cars, **2010 to 2014** models with 12k cars, and **2025** models with 12k cars.
    - The dataset includes the oldest model, a **1919 General Motors Buick Model H**.
    - The majority of car models are from **2024** (1.25k cars), followed by **2021** (22k cars), **2023** (19k cars), and **2022** (16k cars).
    """
    )
    model = df['MODEL'].value_counts().reset_index()
    fig = px.histogram(df['MODEL'],nbins=40)
    st.plotly_chart(fig,use_container_width=True)
    st.write(
    """
    - The majority of cars in the dataset are **Crossovers** (27%), followed by **SUVs** (22%) and **Trucks** (16%).
    - The least common type is **Electric Microcars**, accounting for only 0.0015% of the dataset.
    - Despite a growing number of hybrid and electric models, diesel and petrol cars and trucks still dominate in overall count. Several factors might contribute to this:
      - **Longer Drive Range**: Diesel and petrol engines typically offer a longer drive range and engine life.
      - **Fuel Efficiency**: Diesel trucks, in particular, are known for their torque power and efficiency, which is advantageous for heavy loading.
      - **Consumer Sentiment**: People may still prefer traditional diesel or petrol vehicles due to concerns about the higher cost and longer charging times associated with electric and hybrid cars.
    """
    )
    def combining(row):
        car_type = row['CAR TYPE'].lower()  
        if 'coupe' in car_type:
            return 'coupe'
        elif 'van' in car_type:
            return 'van'
        elif 'suv' in car_type:
            return 'SUV'
        elif 'truck' in car_type:
            return 'Truck'
        elif 'hatchback' in car_type:
            return 'hatchback'
        elif 'sedan' in car_type:
            return 'sedan'
        elif 'wagon' in car_type:
            return 'Wagon'
        elif 'convertible' in car_type:
            return 'convertible'
        else:
            return row['CAR TYPE']  
    temp = df.copy()
    temp['CAR TYPE'] = temp.apply(lambda x : combining(x), axis=1)
    types = temp['CAR TYPE'].value_counts()
    fig = px.pie(types,types.index,types.values,hole=0.4)
    fig.update_traces(textinfo='label+percent')
    st.plotly_chart(fig,use_container_width=True)

    def fuel(row):
        car_type = row['CAR TYPE'].lower()
        if 'electric' in car_type:
            return 'Electric'
        elif 'diesel' in car_type:
            return 'diesel'
        elif 'hybrid'in car_type:
            return 'hybrid'
        else:
            return 'petrol'

    temp1 = df.copy()
    temp1['CAR TYPE'] = temp1.apply(lambda x : fuel(x),axis=1)
    fuels = temp1['CAR TYPE'].value_counts()
    fig = px.pie(fuels,fuels.index,fuels.values,hole=0.4)
    fig.update_traces(textinfo='label+percent')
    st.plotly_chart(fig,use_container_width=True)

    st.write(
    """
    - **51%** of the cars in the dataset are **new**, **45%** are **used**, and the remaining **4%** are **Make Certified**.
    - Among the Make Certified cars, **Mercedes-Benz** leads with **2,000** cars, followed by **Ford** with **900** cars, and **BMW** with **850** cars.
    """
    )
    stocks = df['STOCK TYPE'].value_counts()
    fig = px.pie(stocks,stocks.index,stocks.values)
    st.plotly_chart(fig,use_container_width=True)
    st.write(
    """
    - **7 cars** are marked as **Used** with **0 mileage**, despite their models being old.
    - There are **2 cars** with mileage greater than 0, yet they are marked as **New**. Both cars belong to the same dealer and location, possibly indicating they were used for test drives.
    - **50%** of **used cars** have a mileage range between **27k to 83k**.
    """
    )
    st.write(
    """
    - Most of the car ratings lie between **4 and 5** stars.
    - Some cars had a rating of **-1**, indicating they were not rated yet. To address this, I replaced these values by:
      1. First, using the mean rating of the same **CAR NAME** and **MODEL**.
      2. For any remaining `-1` values, I used the mean rating of the **CAR NAME** alone.
      3. Finally, I filled any further remaining `-1` values using the mean rating of the **MODEL/CLASS**. This approach aimed to provide the most accurate rating possible.
    - It’s not just new cars that have a **5-star** rating; many **Used** and **Certified** cars also achieve this top rating.
    """
    )
    st.write(
    """
    - There are a total of **14,281** unique dealers in the dataset.
    - Many dealers have the **name of a city or state** associated with their business name.
    - **Gateway Classic Cars** has the highest number of cars, totaling **741**.
    - Most of the major dealers primarily offer cars from brands like **BMW**, **Mercedes-Benz**, or **Ford**.
    - Exactly **971** dealers have only **one car** listed with them.
    """
    )
    dealers = df['DEALER NAME'].value_counts().head(50)
    fig = px.bar(dealers,dealers.index,dealers.values)
    st.plotly_chart(fig,use_container_width=True)
    st.write(
    """
    - The dataset includes car data from **3,901 cities and towns** across the US.
    - The majority of car dealers are located in prominent or large cities, such as **Miami**, **Dallas**, and **Las Vegas**.
    - There is very limited car data available for smaller towns and cities in the US.
    - Most cities have **fewer than 500 cars** available for sale.
    """
    )
    city = df['DEALER LOCATION (CITY)'].value_counts()
    fig = px.bar(city.head(20),city.head(20).index,city.head(20).values)
    st.plotly_chart(fig,use_container_width=True)
    st.write(
    """
    - The dataset covers all **50 states** in the US.
    - Similar to cities, most cars are concentrated in **famous or economically powerful states**.
    - **Columbia** has the least number of cars with only **2 cars**, while all other states have at least **400 cars**.
    - **Texas**, **Florida**, and **California** have the highest number of cars, totaling around **75k cars**.
    - States around the **Great Lakes** (e.g., Michigan, Ohio) have a significant number of cars, likely due to extensive trade with Canada and proximity to Canadian capital and industrial cities, which impacts the overall economy.
    - The states with the fewest cars are **Montana**, **Wyoming**, **North Dakota**, and **South Dakota**.
    """
    )

    import json
    us_states = json.load(open("us-states.json", "r"))
    state_id_map = {}
    for feature in us_states['features']:
        state_id_map[feature['properties']['name']] = feature["id"]
    df = df.dropna()
    df['id'] = df['DEALER LOCATION (STATE)'].apply(lambda x :state_id_map[x])
    states = df.groupby(['DEALER LOCATION (STATE)','id'])['CAR ID'].count().reset_index()
    top = states.sort_values('CAR ID',ascending=False)
    fig = px.choropleth_mapbox(
        top,
        locations="id",
        geojson=us_states,
        color="CAR ID",
        hover_name="DEALER LOCATION (STATE)",
        hover_data=["CAR ID"],
        title="STATE WISE RATING",
        mapbox_style="carto-positron",
        center={"lat": 38, "lon": -96.5},
        zoom=3.5,
        opacity=0.6,
    )

    fig.update_layout(
        mapbox_bounds={"west": -125, "east": -66.9, "south": 24.396308, "north": 49.384358},
        margin={"r": 0, "t": 0, "l": 0, "b": 0},  # Remove default margins
    )

    fig.update_geos(
        visible=False,  
        projection_type="albers usa",
    )

    st.plotly_chart(fig,use_container_width=True)
    st.write(
    """
    - The **US car market** is predominantly captured by **US brands** (150k cars), followed by **Japanese brands** (76k) and **German brands** (65k).
    - **Foreign brands** account for **60.5%** of the total market share in the US.
    - The **BMW Group** manages different brands with distinct make origins. For example, the **MINI** brand, acquired by BMW in 1994, and **Rolls-Royce** also falls under BMW’s ownership.
    - Similarly, **Jaguar Land Rover (JLR)**, a British multinational automotive company, was acquired by Tata Motors from Ford in 2008. JLR now operates as a British luxury vehicle manufacturer under Tata’s ownership.
    - The least represented car companies in the dataset are from **South Korea**, **Vietnam**, **France**, and **Sweden**.
    - Among **18 US automobile companies**, the following have ceased operations or no longer exist:
      - **Packard Motor Car Company**
      - **Excalibur Automobile Company**
      - **American Motors Corporation (AMC)**
      - **Bremen**
      - **DeLorean Motor Company**
      - **Studebaker Corporation**
      - **Avanti Motors**
      - **Karma Automotive**
    - From **12 UK automobile companies**, only **British Motor Corporation** no longer exists.
    - The **UK** has the second-largest number of parent companies but a relatively low car count (3,094 cars). This may be due to UK companies primarily manufacturing luxury or high-cost vehicles (e.g., BMW, Lotus, Bentley, Land Rover), leading to lower sales volumes.
    - In contrast, **Japanese** car companies, despite having fewer parent companies than the UK, produce vehicles across all segments, from mid-range (Toyota) to luxury (Lexus, Mazda, Acura). This broad category coverage drives higher sales.
    - **Japanese car brands** dominate the U.S. market due to their **affordability**, **reliability**, **strategic market positioning**, and **local manufacturing**.
    - Despite having only one parent company, **Hyundai Motor Group** (with brands **Kia** and **Hyundai**) performs well in the US market with **11k cars**, outperforming parent companies from the UK, Sweden, and Italy, which have more parent companies comparatively.
    - The top-performing companies within each make origin in terms of car count are:
      - **USA**: **Ford** (Ford Motor Company)
      - **Japanese**: **Toyota** (Toyota Motor Corporation)
      - **Germany**: **Mercedes-Benz** (Daimler AG)
      - **South Korea**: **Hyundai** (Hyundai Motor Group)
      - **UK**: **MINI** (BMW Group)
      - **Sweden**: **Volvo** (Volvo Car Group)
      - **Italy**: **Ferrari** (Ferrari N.V.)
      - **France**: **Bugatti** (Volkswagen Group)
    """
    )
    st.write(
    """
    - Within the entire dataset, as well as specifically within **Ford Motor Company** (the parent company), **Ford** (as a brand) has the highest number of cars.
    - **Mercedes-Benz** leads within **Daimler AG** (the parent company) and **Chevrolet** is the top brand within **General Motors** (the parent company).
    """
    )

    fig = px.sunburst(df,path=['MAKE ORIGIN','PARENT COMPANY','BRAND'])
    st.plotly_chart(fig,use_container_width=True)

    st.write(
    """
    - **Count of Brands by Car Type**:
      - The **Coupe** car type is produced by the highest number of brands, with **60** brands manufacturing this type.
      - This is followed by **Convertible** (52 brands) and **SUV** (47 brands).
      - The least common car types are **Diesel Van**, **Electric Microcar**, and **Coupe SUV**, with specific brands like **Mercedes-Benz**, **Smart**, and **Porsche** manufacturing them, respectively.

    - **Electric/Hybrid Cars** are among the top 10 car types, indicating a growing focus on these vehicles across many car companies.

    - **Correlation Between Number of Brands and Car Units**:
      - The number of brands manufacturing a particular car type does not necessarily correlate with the total number of units for that car type.
        - **Example 1**: Despite **60 brands** producing Coupes, Coupes are ranked **6th** in terms of the total number of cars in the dataset.
        - **Example 2**: **Diesel Trucks**, manufactured by only **3 brands**, rank **2nd** in total number of cars in the dataset.
      - Thus, having many brands manufacturing a particular car type does not always mean that type has the highest number of cars.
    """
    )

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    types = df.groupby('CAR TYPE').agg(
    BRAND_COUNT = ('BRAND','nunique'),
    brands = ('BRAND',set)
    ).sort_values('BRAND_COUNT',ascending=False).reset_index()
    
    type_count = df['CAR TYPE'].value_counts()

    fig = make_subplots(rows=1, cols=2, subplot_titles=("Brand Count by Car Type", "CAR COUNT BY CAR TYPES"))

    fig.add_trace(
        go.Bar(x=types['CAR TYPE'], y=types['BRAND_COUNT']),
        row=1, col=1
    )


    fig.add_trace(
        go.Bar(x=type_count.index, y=type_count.values),
        row=1, col=2
    )


    fig.update_layout(title_text="Comparison of Two Different Charts")

    st.plotly_chart(fig,use_container_width=True)

    st.write(
    """
    - **Price Range**: Most car companies have their prices concentrated between **$30k and $60k**.

    - **High-Priced Cars**:
      - Among the 6 highest-priced cars, **5** are **Bugatti Chiron** models.
      - The top ten highest-priced cars are from brands like **Porsche**, **Bugatti**, **Ferrari**, and **Koenigsegg**.

    - **Outlier Values**: All outlier values have been cross-checked and are justified.

    - **Top Brands**:
      - In the top 100 brands, **5** brands are actively operating: **Ferrari**, **Lamborghini**, **Porsche**, **Bugatti**, **Mercedes-Benz**, and **Koenigsegg**.
      - Most of the stock from these brands is categorized as **Used cars** (75) and **Certified cars** (33), with only **2 new cars**.

    - **New vs. Model Year**: A "new" car doesn't necessarily have to be a 2024 or 2025 model. Older models can be termed "new" if they have zero mileage.

    - **Cheapest Cars**:
      - The cheapest new car in the dataset is the **Chevrolet Traverse LT Cloth 2019** model, priced at **$10,995**.
      - For 2024 and new models, the cheapest car is the **Mitsubishi Mirage ES**, priced at **$15,910**.

    - **High-Priced Cars by State**:
      - The 50 highest-priced cars are concentrated in **Florida**, **California**, **North Carolina**, and **Texas**.

    - **Average Price by State**:
      - A function has been created to find the average price of new cars in different states.
        - For example, the **Toyota GR86 Base** is priced least in **Idaho** (around **$29k**) and highest in **California** (around **$39k**).
    """
    )

    fig = px.box(df,df['PRICE($)'],hover_name='BRAND')
    st.plotly_chart(fig,use_container_width=True)
    st.write(
    """
    - **Certified Cars**:
      - **Certified Cars** are used vehicles that have undergone thorough inspections and refurbishment by the manufacturer or an authorized dealership, ensuring they meet high standards of quality and reliability.
      - **Mileage and Age**: Most certified cars are between 0 to 5 years old (up to 9 years) and have mileage around 70k to 90k, which is lower than the average used car.

    - **Top Certified Cars**:
      - **Mercedes-Benz Certified** cars lead with the highest number (2056), followed by **Ford** (910), **BMW** (857), and **Audi** (855).
      - **Least Certified Cars**: Brands like **FIAT**, **RAM**, **Maserati**, and **Polestar** have the fewest certified cars.

    - **Price Trends**:
      - **Price vs. Age**: There is a negative linear correlation between price and age for the first 15 years, meaning prices generally decrease as cars age. After 15 years, there is no clear linear correlation due to fluctuations caused by unique conditions of some vehicles.
      - **Certified vs. Used Cars**: Certified cars typically cost more than used cars due to the inspection, repair, and certification process, which adds value.

    - **Luxury Cars and Certification**:
      - **Luxury Cars**: These cars tend to have more certified vehicles due to higher depreciation rates. Certified programs help mitigate this depreciation by offering slightly used luxury vehicles at more attractive prices.
        - **Example 1**: **Porsche Cayenne** 2024 model shows a price difference of $10,000 between new and used vehicles.
        - **Example 2**: **Chevrolet Silverado 1500 Custom** 2024 model has a price difference of about $2,000.
      - **Reputation**: Luxury brands use certification to maintain their reputation, ensure high-quality standards, and manage their lease returns effectively.
    """
    )

    age_price = df.groupby('AGE OF CAR')['PRICE($)'].mean()
    fig = px.line(age_price,age_price.index,age_price.values)
    st.plotly_chart(fig,use_container_width=True)

    stocks = df['STOCK TYPE'].value_counts()
    fig = px.bar(stocks,stocks.index,stocks.values,text_auto=True)
    st.plotly_chart(fig,use_container_width=True)

    st.write(
    """
    - **Hybrid Hatchbacks**:
      - Surprisingly, **Hybrid Hatchbacks** have the highest average mileage. This might be due to their affordability and suitability for middle-class Americans who prioritize fuel efficiency and cost-effectiveness.

    - **Other Car Types**:
      - **Wagons**, **Minivans**, and **Traditional Fuel Trucks** (petrol and diesel) follow in terms of high mileage. These vehicles are often used for commercial purposes, transportation of goods, and logistics, which justifies their higher mileage compared to luxury vehicles.

    - **Electric/Hybrid Trucks and Vans**:
      - **Electric and Hybrid Trucks** and **Electric Vans** have lower mileage compared to their traditional counterparts. This is because electric and hybrid trucks, despite their growing capabilities, often lag in range and towing power compared to diesel or petrol trucks, which have long been preferred for heavy-duty tasks.

    - **Brand Origin**:
      - Most of the top-performing car brands in terms of mileage are from **US origin**, with **Ford** and **Chevrolet** being the most common. This indicates a strong performance by US-based manufacturers in producing high-mileage vehicles.
    """
    )
    st.write(
    """
    - **Crossover Cars**:
      - Most states feature **Crossover** vehicles prominently. **Florida** stands out with the highest number of both cars and crossovers.

    - **Diesel Trucks**:
      - **Diesel Trucks** are most common in states such as **Mississippi**, **Arkansas**, **Idaho**, **Oregon**, **Montana**, **South Dakota**, **Alaska**, and **Wyoming**. Reasons include:
        - **Rural and Agricultural Regions**: Many of these states have significant rural areas where diesel trucks are essential for agricultural and heavy-duty work.
        - **Lower Population Densities**: Larger land areas with fewer people make trucks ideal for covering long distances and handling rugged terrains.
        - **Outdoor Activities**: States known for activities like hunting, fishing, and off-roading often see higher truck usage.
        - **Adverse Weather Conditions**: Colder climates and heavy snowfall in states like Alaska and Wyoming contribute to the higher prevalence of trucks, which are better suited for challenging weather conditions and rough roads.

    **Source**: Google.
    """
    )



    st.header('DIFFERENCE BETWEEN CAR TYPES')
    st.markdown("""
| **Category**    | **Definition**                                                              | **Body Style**                 | **Passenger Capacity** | **Cargo Space**                | **Common Features**                                                | **Typical Use Case**                           |
|-----------------|-----------------------------------------------------------------------------|--------------------------------|------------------------|--------------------------------|-------------------------------------------------------------------|-------------------------------------------------|
| **Crossover**   | Combines features of an SUV and a car, often built on a unibody frame.      | Unibody, higher ground clearance | 5-7                    | Moderate                       | Car-like handling, often front-wheel or all-wheel drive           | Daily commuting, light off-road, family use     |
| **Convertible** | A car with a roof that can be folded down or removed for open-air driving.  | Typically two-door, with a retractable roof | 2-4               | Limited                        | Sporty design, available as soft-top or hard-top                  | Leisure driving, sporty experience             |
| **Coupe**       | A car with a fixed-roof body style, usually with two doors.                 | Two-door, sleek design         | 2-4                    | Limited                        | Sporty appearance, sloping roofline                               | Sporty driving, urban use                      |
| **SUV**         | A sport utility vehicle with both on-road and off-road capabilities.        | High ground clearance, often body-on-frame | 5-7               | Ample                          | Available in various sizes, all-wheel or four-wheel drive         | Family use, off-road, towing                   |
| **Hatchback**   | A car with a rear door that swings upward to access the cargo area.         | Compact, often 3 or 5-door     | 4-5                    | Versatile, expandable with foldable rear seats | Compact design, efficient use of space        | Urban commuting, small families                |
| **Sedan**       | A car with a separate compartment for the engine, passengers, and cargo.    | Four-door, three-box design    | 4-5                    | Moderate, separate trunk        | Balanced design, comfortable ride                                  | Daily commuting, family use, business           |
| **Wagon**       | A car with an extended roofline and a hatch door at the rear for more cargo space. | Longer body, five-door  | 5-7                    | Generous, flat cargo area       | Spacious, often includes roof rails                                | Family use, long-distance travel, outdoor activities |
""")
    

def dataset():
    st.markdown(
        """
## **Creating the Dataset: Web Scraping for Car Data**

### **1. Setting Up the Environment**

To begin the data collection process, I utilized several Python libraries, each playing a crucial role in web scraping and data handling:

- **Selenium**: Automated browser interactions to navigate and retrieve data from multiple pages of the website.
- **BeautifulSoup**: Parsed HTML content to extract specific elements such as car details.
- **Pandas**: Organized and stored the extracted data into a structured format.
- **NumPy**: Handled any necessary data manipulation and cleaning.
- **Requests**: Managed HTTP requests during the scraping process.

### **2. Configuring Selenium WebDriver**

I configured Selenium using the Chrome WebDriver to automate the process of visiting the car website. The following steps were involved:

- **WebDriver Initialization**: Set up the Chrome WebDriver with specific options, including the path to the `chromedriver.exe`.
- **Page Navigation**: Directed the browser to the target URL, which lists cars for sale. I used pagination to navigate through multiple pages to gather extensive data.

```python
s = Service("chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options, service=s)
driver.get('https://www.cars.com/shopping/results/?dealer_id=&fuel_slugs[]=electric&include_shippable=false&keyword=&list_price_max=&list_price_min=&makes[]=&maximum_distance=all&mileage_max=&monthly_payment=&page=1&page_size=100&sort=best_match_desc&stock_type=all&year_max=&year_min=&zip=60606')
```

### **3. Scraping Data from the Website**

With the browser automated, I scraped the required data using BeautifulSoup. The scraping process involved:

- **Extracting HTML Content**: Retrieved the page’s source code using Selenium and parsed it with BeautifulSoup.
  
- **Data Extraction**: Collected various data points such as car names, images, prices, stock types, mileage, ratings, reviews, dealer names, and locations. For each data point, I handled potential errors by assigning default values (e.g., `np.nan`) when data was missing or inaccessible.

```python
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

# Example of extracting car names and images
for i in soup.find_all('div', {'class': 'image-wrap', 'data-index': '0'}):
    name.append(i.find('img').get('alt'))
    image.append(i.find('img').get('src'))
```

### **4. Handling Dynamic Content and Pagination**

I iterated over multiple pages to scrape a comprehensive dataset. This involved:

- **Looping Through Pages**: Automated the process of moving through pages by modifying the page number in the URL.
- **Delay Implementation**: Used `time.sleep()` to ensure that the website loaded fully before scraping data, avoiding any potential data loss.

```python
for i in range(1, 10):
    driver.get(f'https://www.cars.com/shopping/results/?page={i}&page_size=100&sort=best_match_desc')
    time.sleep(3)
    # Scraped data here
```

### **5. Organizing Data into a DataFrame**

After scraping the data, I compiled it into a Pandas DataFrame for easy manipulation and analysis. This step involved:

- **Data Structuring**: Each extracted element (e.g., car name, price) was appended to respective lists, which were later used to populate the DataFrame columns.
  
- **Data Cleaning**: Ensured that the DataFrame was free of inconsistencies, such as missing values, by using placeholders like `np.nan`.

```python
df = pd.DataFrame({
    'Name': name,
    'Image': image,
    'Price': price,
    'Stock Type': stock_type,
    'Mileage': mileage,
    'Rating': rating,
    'Review': review,
    'Dealer Name': dealer_name,
    'Dealer Location': dealer_location
})
```

### **6. Conclusion**

This systematic approach to web scraping enabled the creation of a rich dataset around 20,00,000 unique datapoints containing detailed information on various cars listed on the website. The combination of Selenium for browsing automation and BeautifulSoup for content extraction, supported by Pandas and NumPy for data management, proved to be highly effective. This dataset serves as the foundation for further analysis and visualization in my project.
```
    """
    )

    st.subheader('DOWNLOAD DATASET')
    st.write('You can download the dataset from my kaggle profile.')
    st.markdown(f'<a href="{'https://www.kaggle.com/datasets/akshatsharma2407/cars-dataset'}" target="_blank">DATASET LINK</a>',unsafe_allow_html=True)

def me():
    st.header('ABOUT ME!')
    st.markdown("""
I am an aspiring data scientist with a strong passion for storytelling. I believe that words and data are two of the most powerful tools to drive meaningful change.

I spend most of my time honing my skills in programming and extracting insights from large datasets. My focus areas include data analysis, visualization, and machine learning. I love solving problems, and I'm always up for a challenge. My work often involves end-to-end data science projects, where I get to apply and expand my knowledge.

In the evenings, I shift my focus to the things I’m truly passionate about. I write articles and blogs, sharing my learning journey with others online. I also enjoy working on personal projects and creating tutorials to help others in the community. Sites like HackerRank,CampusX are a great source of practice, and I frequently engage in their programming challenges to sharpen my skills.

To give back to the community, I create tutorials and blogs on data science and Python, which I publish for everyone to access. If you're an aspiring data scientist like me, I invite you to explore these tutorials on Medium.
""")
    st.markdown("""
    ### Connect with Me

    - **Medium:** [Follow me on Medium](https://medium.com/@akshatsharma5877)
    - **LinkedIn:** [Connect with me on LinkedIn](https://www.linkedin.com/in/akshat-sharma-89635631b/)
    - **Email:** [akshatsharma5877@gmail.com]
    """)



# Render the selected section
if option == 'Home':
    home()

elif option == 'Search by Brand':
    st.empty()
    brand = st.sidebar.selectbox('BRAND',sorted(df['BRAND'].unique()))
    print(brand,'*'*100)
    model_list = df[df['BRAND'] == brand]['MODEL/CLASS'].unique()
    print(model_list)
    selected_model = st.sidebar.selectbox('MODEL',model_list)
    search_by_brand(brand,selected_model)

elif option == 'Search by Category':

    category = st.sidebar.selectbox('CATEGORY',sorted(df['CAR TYPE'].unique()))
    price_set = df[df['CAR TYPE'] == category]['PRICE($)']
    lower_limit = st.sidebar.slider('SET LOWER LIMIT ON PRICE',round(price_set.min()),round(price_set.max()))
    upper_limit = st.sidebar.slider('SET UPPPER LIMIT ON PRICE',round(price_set.min()),round(price_set.max()),value=round(price_set.max()))

    limit_set = df[(df['CAR TYPE'] == category) & (df['PRICE($)'] >= lower_limit) & (upper_limit >= df['PRICE($)'])]

    states = sorted(limit_set['DEALER LOCATION (STATE)'].unique().tolist())
    states =  ['SELECT ALL'] + states 

    state = st.sidebar.multiselect('SELECT STATE',states,default=['SELECT ALL'])

    if 'SELECT ALL' in state:
        cities = sorted(limit_set['DEALER LOCATION (CITY)'].unique().tolist())
        cities = ['SELECT ALL'] + cities
        city = st.sidebar.multiselect('SELECT CITY',cities,default=['SELECT ALL'])
        
    else:
        if 'SELECT ALL' in state:
            state.remove('SELECT ALL')

        cities = sorted(limit_set[limit_set['DEALER LOCATION (STATE)'].apply(lambda x : x in state)]['DEALER LOCATION (CITY)'].unique())

        limit_set = limit_set[limit_set['DEALER LOCATION (STATE)'].apply(lambda x : x in state)]

        cities = ['SELECT ALL'] + cities

        city = st.sidebar.multiselect('SELECT CITY',cities,default=['SELECT ALL'])
    
    if 'SELECT ALL' in city:
        pass
    else:
        if 'SELECT ALL' in city:
            city.remove('SELECT ALL')
        limit_set = limit_set[limit_set['DEALER LOCATION (CITY)'].apply(lambda x : x in city)]
    search_by_category(limit_set)

elif option == 'EDA':
    EDA(df)

elif option == 'ABOUT ME':
    me()

else:
    dataset()
