"""Customer support response engine. No terminal input is used by the Flask app."""
import random
import re


class SupportBot:
    """Keyword-based customer support chatbot."""

    def __init__(self):
        self.support_responses = {
            "ask_about_product": r"\b(product|products|price|cost|item|items|catalog|catalogue)\b",
            "technical_support": r"\b(technical|support|error|issue|problem|bug|not working|trouble)\b",
            "about_returns": r"\b(return|refund|exchange|return policy|refund policy)\b",
            "general_query": r"\b(help|how can you help|what can you do|services)\b",
            "order_status": r"\b(order|delivery|shipping|tracking|track)\b",
        }

    def match_reply(self, message: str) -> str:
        """Return a response for one message; safe to call from a web request."""
        text = (message or "").lower().strip()
        if not text:
            return "Please type a message so I can help you."

        if re.search(r"\b(hello|hi|hey|good morning|good afternoon|good evening)\b", text):
            return "Hello! Welcome to customer support. How can I help you today?"
        if re.search(r"\b(thank you|thanks|thx)\b", text):
            return "You're welcome! Is there anything else I can help you with?"
        if re.search(r"\b(bye|goodbye|quit|exit)\b", text):
            return "Thanks for contacting customer support. Have a great day!"

        for intent, pattern in self.support_responses.items():
            if re.search(pattern, text):
                if intent == "ask_about_product":
                    return self.ask_about_product()
                if intent == "technical_support":
                    return self.technical_support()
                if intent == "about_returns":
                    return self.about_returns()
                if intent == "general_query":
                    return self.general_query()
                if intent == "order_status":
                    return self.order_status()

        return self.no_match_intent()

    @staticmethod
    def ask_about_product() -> str:
        return random.choice([
            "Our products are designed for quality and reliability. Which product would you like to know about?",
            "You can find product details on our website. Tell me the product name and I can guide you.",
        ])

    @staticmethod
    def technical_support() -> str:
        return random.choice([
            "I'm sorry you're facing a technical issue. Please describe the error and tell me which product or service you're using.",
            "Please share the steps that caused the issue and any error message you see. I'll help you troubleshoot.",
        ])

    @staticmethod
    def about_returns() -> str:
        return random.choice([
            "Our sample return policy allows returns within 30 days. Please check the seller's official policy for the exact conditions.",
            "For a return or refund, keep your order details and product condition ready, then contact the support team.",
        ])

    @staticmethod
    def general_query() -> str:
        return "I can help with product information, technical support, returns, refunds, and order tracking. What do you need help with?"

    @staticmethod
    def order_status() -> str:
        return "I can help with order tracking. Please check your order confirmation for the tracking ID, or contact the store's order support team."

    @staticmethod
    def no_match_intent() -> str:
        return "I'm sorry, I didn't quite understand that. Could you rephrase your question or ask about products, technical support, returns, or orders?"
