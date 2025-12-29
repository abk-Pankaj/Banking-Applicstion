# 🏦 ABC Bank – Simple Banking Application

## 📌 Description
ABC Bank is a **console-based Python application** that simulates basic banking operations. It allows users to **sign up, log in, and manage their accounts** with simple features like checking balance, depositing money, and withdrawing funds.  

The program is designed to demonstrate:
- **User registration & login system**  
- **Account balance management**  
- **Safe withdrawal logic (no negative balances)**  
- **Interactive menu-driven interface**

---

## ⚙️ Features
- 👤 **User Registration**: New customers can sign up by providing their name and age.  
- 🔑 **Login System**: Registered customers can log in with their details.  
- 💰 **Check Balance**: Displays the current account balance.  
- ➕ **Deposit Money**: Add funds to your account.  
- ➖ **Withdraw Money**: Withdraw funds safely (prevents overdraft).  
- 🚪 **Exit Option**: End the session gracefully.  

---

## 🛡️ Safety in Withdrawals
The withdrawal function ensures:
- No negative withdrawal amounts.  
- No overdraft — users cannot withdraw more than their current balance.  
- Clear error messages for invalid transactions.  

---

## ▶️ How to Run
1. Save the script as `banking_app.py`.  
2. Run in terminal/command prompt:  
   ```bash
   python banking_app.py
   ```
3. Follow the on-screen instructions to **login or sign up** and start banking.  

---

## 📚 Example Flow
```
Welcome To ABC Bank
If you are a registered customer please login or if you are new please Sign Up
1. Login
2. Sign up
Enter your option(1-2): 1
Enter your name: Pankaj
Enter your age: 18
Welcome back, Pankaj!

Choose an option:
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
```

---

## 🚀 Future Improvements
- Add multiple accounts per user.  
- Implement PIN/password authentication.  
- Save customer data permanently (e.g., using files or databases).  
- Add transaction history tracking.
