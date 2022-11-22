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

- **Trigger:**

- **Primary Sequence:**
  
  1. 
  2. 
  3. 
  4.  
  5. 
  6. 
  7. 
  8. 
  9. 
  10. 

- **Primary Postconditions:**

- **Alternate Sequence:**
  
  1. 
  2. 
  3. 

- **Alternate Sequence:**
  
  1. 
  2. 
  3. 

2. Send message to followers
- **Pre-condition:**

- **Trigger:**

- **Primary Sequence:**
  
  1. 
  2. 
  3. 
  4.  
  5. 
  6. 
  7. 
  8. 
  9. 
  10. 

- **Primary Postconditions:**

- **Alternate Sequence:**
  
  1. 
  2. 
  3. 

- **Alternate Sequence:**
  
  1. 
  2. 
  3. 

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
- **Pre-condition:** 

- **Trigger:** 

- **Primary Sequence:**
  
  1. 
  2. 
  3. 
  4.  
  5. 
  6. 
  7. 
  8. 
  9. 
  10. 

- **Primary Postconditions:** 

- **Alternate Sequence:** 
  
  1. 
  2. 
  3. 

- **Alternate Sequence:** 
  
  1. 
  2. 
  3. 

6. Search messages
- **Pre-condition:** 

- **Trigger:** 

- **Primary Sequence:**
  
  1. 
  2. 
  3. 
  4.  
  5. 
  6. 
  7. 
  8. 
  9. 
  10. 

- **Primary Postconditions:** 

- **Alternate Sequence:** 
  
  1. 
  2. 
  3. 

- **Alternate Sequence:** 
  
  1. 
  2. 
  3. 
