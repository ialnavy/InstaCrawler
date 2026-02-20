class InstagramSelectors:

    instagram_home_url = "https://www.instagram.com/"
    
    # Instagram log-in elements
    input_username = "input[name*=\"username\"]"
    register_button = "a[href*=\"emailsignup\"]"
    profile_button = "body > div:first-of-type > div > div > div:nth-of-type(2) > div > div > div:first-of-type > div:first-of-type > div:first-of-type > div > div > div > div > div > div:nth-of-type(2) > div > div:last-of-type > div > span > div > a"

    # Profile page elements
    logged_user_id= "body > div:first-of-type > div > div > div:nth-of-type(2) > div > div > div:first-of-type > div:nth-of-type(2) > div:first-of-type > section > main > div > div > header > section:nth-of-type(2) > div > div > div:first-of-type > div > a > h2 > span"

    followers_link = "a[href*=\"followers\"]"
    following_link = "a[href*=\"following\"]"

    scrollable_div = "body > div:last-of-type > div:last-of-type > div:first-of-type > div:first-of-type > div:first-of-type > div:first-of-type > div:nth-of-type(2) > div:first-of-type > div:first-of-type > div:first-of-type > div:first-of-type > div:last-of-type > div:first-of-type > div:first-of-type > div:last-of-type"
    container_of_users = "body > div:last-of-type > div:last-of-type > div:first-of-type > div:first-of-type > div:first-of-type > div:first-of-type > div:nth-of-type(2) > div:first-of-type > div:first-of-type > div:first-of-type > div:first-of-type > div:last-of-type > div:first-of-type > div:first-of-type > div:last-of-type > div:first-of-type > div:first-of-type"
    
    user_id_1 = 'div > div > div > div:nth-of-type(2) > div > div > div:first-of-type > div > span > div > a > div > div > span'
    user_id_2 = 'div > div > div > div:nth-of-type(2) > div > div > div:first-of-type > a > div > span > div'
    user_full_name = 'div > div > div > div:nth-of-type(2) > div > div > span:last-of-type > span'
