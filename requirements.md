## Functional Requirements

1. Login                                                        - @giftolatunji
2. Logout                                                       - @giftolatunji
3. Create new account                                           - @giftolatunji
4. delete account                                               - @giftolatunji
5. User home page (user can see messages of users they follow)  - @eacarrasco
6. Send message to followers                                    - @eacarrasco
7. Like message                                                 - @eacarrasco
8. Follow User                                                  - @eacarrasco
9. Search for user                                              - @LofiTurtle
10. Search messages                                             - @LofiTurtle
11. Splash page                                                 - @LofiTurtle
12. Connect with any external API                               - @LofiTurtle

## Non-functional Requirements

1. Only expected to work on Google Chrome and Firefox
2. Each page should load in under 1 second
3. Error rate if submitting new messages should be below 5%
4. Website should be able to handle 100s of users

## Use Cases

1. User home page
- **Pre-condition:**
The User has an account
- **Trigger:**
User selects login button
- **Primary Sequence:**
  
  1. System prompts the user to enter email address and password information
  2. User enters an email address assosciated with their account and password to access it
  3. System checks with database if it is correct username and password
  4. System allows the user to login and shows the home page. 

- **Primary Postconditions:**
System displays the home page
- **Alternate Sequence:**
  The User enters wrong username or password
  1. The system displays an error message to the User
  2. The system Prompts the user to enter a valid username and/or password in the login page

- **Alternate Sequence:**
  The user does not have an account
  1. The system displays an error message
  2. The system directs the User to the login page where there is a create an account button

2. Send message to followers
- **Pre-condition:**
The user has followers
- **Trigger:**
User selects message follower
- **Primary Sequence:**
  
  1. System prompts the user to select follower they would like to message
  2. Customer selects the follower to be messaged
  3. System checks that the follower is currently following our user
  4. System directs the user to enter message in a text box
  5. User types in message in text box
  6. User sends message by hitting the send button
  7. System sends message to follower
  
- **Primary Postconditions:**
System successfully sends message to the follower

- **Alternate Sequence:**
The user has no follower 
  1. The system displays an error message to the User
  2. The system prompts the user to obtain valid followers

- **Alternate Sequence:**
The follower to be messaged no longer follows the user
  1. The system displays a prompt that the follower is no longer available to be messaged
  2. The system prompts the user to message another follower

3. Like message
- **Pre-condition:**

- **Trigger:**

- **Primary Sequence:**
  
  1. User clicks messages
  2. User sends message or recieves message (See Use Case "Send message to followers")
  3. User clicks heart next to message

- **Primary Postconditions:** A message is liked.

- **Alternate Sequence:**
  
  1. User has no messages

    a. There will be no heart to click

4. Follow User
- **Pre-condition:** User is logged in and has searched for a user.

- **Trigger:** User clicks the Follow button on another user's homepage.

- **Primary Sequence:**
  
  1. User searches for another user (See use case "Search for User")
  2. User clicks on desired user and is directed to their homepage
  3. User clicks the Follow button on their homepage

- **Primary Postconditions:** User's following list is updated

- **Alternate Sequence:**
  
  1. Search for user that does not exist.

    a. A blank page is shown.

5. Search for user
- **Pre-condition:** Viewing the splash screen or home page.

- **Trigger:** User selects the search field.

- **Primary Sequence:**
  
  1. User inputs some text into the search box
  2. User selects the “Search users” box from a radio menu (as opposed to the “search messages” box)
  3. User selects the search button, or presses Enter on the keyboard
  4. User is redirected to a page where profiles whose usernames contain the text sequence entered by the user are listed

- **Primary Postconditions:** System displays the list of search results.

- **Alternate Sequence:** The user enters text that does not match any username.
  
  1. User is redirected to a page displaying an error message that no users were found

- **Alternate Sequence:** The user does not enter text before selecting search.
  
  1. A popup appears, prompting the user to enter some text into the search field

1. Slpash page
- **Pre-condition:** User is not logged in.

- **Trigger:** User visits the website homepage while not logged in.

- **Primary Sequence:**
  
  1. User sees a page with a random background image from Unsplash, and buttons to log in, register an account, and search for users or messages

- **Primary Postconditions:** The user is on the splash page, and is able to login, create an account, or search for messages.

- **Alternate Sequence:** Unsplash API is unable to provide an image.
  
  1. User sees the splash screen with a solid-color background instead of an image
