import streamlit as st

# TASK 1 - UI Shell
st.title("Echo Chamber 9000")
st.write("Enter your name and a message, then click Transmit.")

# TASK 2 - Multi-Data Collection
user_name = st.text_input("Name")
user_message = st.text_input("Message")

# TASK 3 - The Action Gate
submitted = st.button("Transmit")

if submitted:
    # TASK 4 - Conditional Routing (Edge Cases)
    if not user_name:
        st.error("Please provide your name.")
    elif not user_message:
        st.warning("Please type a message to transmit.")
    else:
        # TASK 5 - Formatted Output
        st.success(f"Transmission successful! Greetings, {user_name}. We received your message: {user_message}")

        # ADVANCED CHALLENGE - Token Estimation
        char_length = len(user_message)
        token_count = char_length // 4
        st.info(f"System Check: Your message will consume approximately {token_count} tokens from our context window.")
