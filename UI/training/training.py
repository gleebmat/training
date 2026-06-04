import reflex as rx
import sys
import os

sys.path.append(os.path.abspath('..'))

from calc import calculate

# The State (a class that holds the state of the site)
class AppVar(rx.State):

    # --- Calculator state variables ---
    num_1: str = ""
    num_2: str = ""
    operation: str = "Add (+)"
    calc_result: str = ""

    calc_operations: list[str] = [
        "Add (+)", "Subtract (-)", "Multiply (*)", "Divide (/)", 
        "Power (**)", "Root", "Factorial", "Sin", "Cos", "Tan", "Log"
    ]

    @rx.var
    def req_two_numbers(self) -> bool:
        single_input_ops = {"Factorial", "Sin", "Cos", "Tan", "Log"}
        return self.operation not in single_input_ops

    def perform_calculation(self):
        op_map = {
            "Add (+)": "1",
            "Subtract (-)": "2",
            "Multiply (*)": "3",
            "Divide (/)": "4",
            "Power (**)": "5",
            "Root": "6",
            "Factorial": "7",
            "Sin": "8",
            "Cos": "9",
            "Tan": "10",
            "Log": "11"
        }

        choice = op_map.get(self.operation, "1")

        try:
            a = float(self.num_1) if self.num_1 else 0
            b = float(self.num_2) if self.num_2 else 0

            if choice == "7":  # Factorial only uses num_1
                a = int(a)  # Factorial should be an integer

            result = calculate(a, b, choice)

            if result is None:
                self.calc_result = "Invalid operation."
            else:
                self.calc_result = str(round(result, 5))
        
        except ZeroDivisionError:
            self.calc_result = "Error: Div by 0"
        except ValueError:
            self.calc_result = "Error: Invalid Math"
        except Exception as e:
            self.calc_result = "Error"
    
    def set_num_1(self, value):
        self.num_1 = value
    
    def set_num_2(self, value):
        self.num_2 = value

    def set_operation(self, value):
        self.operation = value

    # --- Q&A Agent state variables ---
    current_question: str = ""
    chat_history: list[tuple[str, str]] = [
        ("Test question?", "Test answer.")
    ]  # List of (question, answer) pairs

    # --- Image Generation state variables ---
    image_prompt: str = ""
    image_url: str = "https://via.placeholder.com/400x300.png?text=Waiting+for+prompt..."

    # --- Voice Assistant state variables ---
    is_listening: bool = False
    spoken_text: str = ""

    def dummy_method(self):
        pass
    
    def toggle_recording(self):
        self.is_listening = not self.is_listening
        if self.is_listening:
            self.spoken_text = "Listening... (simulated)"
        else:
            self.spoken_text = "Stopped listening."

    pass

# The UI of the calculator
def calculator_view():
    return rx.card(
        rx.heading("Calculator", size="4", margin_bottom="1em"),

        # The output display
        rx.box(
            rx.text(AppVar.calc_result, size = "6", text_align="center", color_scheme="blue"),
            padding="1em",
            border="1px solid var(--gray-5)",
            border_radius="medium",
            margin_bottom="1em",
            background_color="var(--gray-3)",
        ),

        # The Input fields and operation selector
        rx.hstack(
            rx.input(placeholder="Number 1", type="number", on_change =AppVar.set_num_1, width="100%"),
            rx.select(AppVar.calc_operations, value=AppVar.operation, on_change=AppVar.set_operation),
            rx.cond(
                AppVar.req_two_numbers,
                rx.input(placeholder="Number 2", on_change=AppVar.set_num_2, width="100%"),
            ),
            width="100%", spacing="2", margin_bottom="1em",
        ),
        rx.button("Calculate", on_click=AppVar.perform_calculation, width="100%", size = "3"),
        width="100%",
        max_width="500px",
        margin="auto",     
    )

# The UI of the Q&A agent
def qa_agent_view():
    return rx.card(
        rx.heading("Q&A Agent", size="4"),
        rx.text("Q&A Agent components will go here", color_scheme="gray"),
        # The components for the Q&A agent will go here
        height="60vh",
    )

# The UI of image generation
def image_generation_view():
    return rx.card(
        rx.heading("Image Generation", size="4"),
        rx.text("Image Generation components will go here", color_scheme="gray"),
        # The components for image generation will go here
    )   

# Voice assistant view 
def voice_assistant_view():
    return rx.card(
        rx.heading("Voice Assistant", size="4"),
        rx.text("Voice Assistant components will go here", color_scheme="gray"),
        # The components for the voice assistant will go here
    ) 

# The main page assembly
def index():
    return rx.container(
        rx.heading("AI Multitool", size="8", margin_bottom="1em", text_align="center"),

        # The tabbed navigation
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Calculator", value="calc"),
                rx.tabs.trigger("Q&A Agent", value="qa"),
                rx.tabs.trigger("Image Generation", value="img"),
                rx.tabs.trigger("Voice Assistant", value="va"),
                justify_content="center",
                margin_bottom="2em",
            ),
            # Each content block sits on its own
            rx.tabs.content(calculator_view(), value="calc"),
            rx.tabs.content(qa_agent_view(), value="qa"),
            rx.tabs.content(image_generation_view(), value="img"),
            rx.tabs.content(voice_assistant_view(), value="va"),
            default_value="qa",
        ),
        padding="2em",
    )

# The site initialization
app = rx.App(
    # FIXED: Spelling of appearance and radius name
    theme=rx.theme(appearance="dark", accent_color="blue", radius="medium")
)
app.add_page(index)