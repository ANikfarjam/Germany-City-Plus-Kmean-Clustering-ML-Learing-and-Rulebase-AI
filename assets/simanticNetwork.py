#author: ashkan Nikfarjam
from manim import *

class SemanticNetworkAnimation(Scene):
    def construct(self):
        # Create nodes
        sarah = Text("Sarah").shift(LEFT * 3 + UP * 2)
        joe = Text("Joe").shift(RIGHT * 3 + UP * 2)
        apple = Text("Fuji Apple").shift(LEFT * 3 + DOWN)
        fruit = Text("Fruit").shift(RIGHT * 3 + DOWN)
        gave = Text("gave").shift(UP)

        # Create edges
        sarah_gave = Arrow(sarah.get_bottom(), gave.get_top() + LEFT * 0.5, buff=0.1, color=BLUE)
        gave_apple = Arrow(gave.get_bottom() + RIGHT * 0.5, apple.get_top(), buff=0.1, color=BLUE)
        apple_joe = Arrow(apple.get_right(), joe.get_bottom(), buff=0.1, color=RED)
        is_a = Arrow(apple.get_right(), fruit.get_left(), buff=0.1, color=GREEN)
        cousin = Text("cousin", font_size=24).next_to(apple_joe, DOWN)
        is_a_label = Text("is_a", font_size=24).next_to(is_a, DOWN)

        # Create semantic network
        semantic_network = VGroup(
            sarah, joe, apple, fruit, gave,
            sarah_gave, gave_apple, apple_joe, is_a, cousin, is_a_label
        )

        # Animate the construction of the semantic network
        self.play(
            LaggedStart(
                FadeIn(sarah),
                FadeIn(joe),
                FadeIn(apple),
                FadeIn(fruit),
                FadeIn(gave),
                lag_ratio=0.5
            )
        )
        self.wait()

        self.play(
            LaggedStart(
                GrowArrow(sarah_gave),
                GrowArrow(gave_apple),
                GrowArrow(apple_joe),
                GrowArrow(is_a),
                FadeIn(cousin),
                FadeIn(is_a_label),
                lag_ratio=0.5
            )
        )
        self.wait(2)

# Run the animation
if __name__ == "__main__":
    scene = SemanticNetworkAnimation()
    scene.render()