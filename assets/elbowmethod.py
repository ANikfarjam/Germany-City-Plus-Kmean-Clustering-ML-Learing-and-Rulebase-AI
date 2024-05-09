
from manim import *

class ElbowPlot(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 100, 20],
            x_length=6,
            y_length=4,
            tips=False,
        )
        self.play(Create(axes))

        # Plot data points
        data = [80, 60, 45, 35, 30, 28, 26, 24, 22, 20]
        points = [
            axes.coords_to_point(x, y)
            for x, y in enumerate(data, start=1)
        ]
        elbow_plot = VMobject().set_points_as_corners(points)
        self.play(Create(elbow_plot))

        # Add arrow pointing to the elbow
        elbow_point = points[3]  # Assuming the elbow is at k=4
        arrow = Arrow(
            start=elbow_point + LEFT * 2,
            end=elbow_point,
            buff=0.1,
            max_tip_length_to_length_ratio=0.3
        )
        self.play(Create(arrow))

        # Label axes
        x_label = Text("Number of clusters (k)").next_to(axes.x_axis, DOWN)
        y_label = Text("WCSS").next_to(axes.y_axis, LEFT).rotate(PI/2)
        self.play(Write(x_label), Write(y_label))
        self.wait()