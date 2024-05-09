#author: Ashkan Nikfarjam
#to run this file individually use the following command
# python3 -m manim -pql animmation.py KMeansClusteringAnimation
from manim import *
import random
import numpy as np
from scipy.spatial import ConvexHull

class KMeansClusteringAnimation(Scene):
    def construct(self):
         # Create a circle with blurred color
        circle = Circle()
        circle.set_fill(color=PINK, opacity=0.3)  # Adjust opacity for blur effect

        # Show the circle on screen
        self.play(Create(circle))

        # Add a title aligned in the center of the circle
        title = Text("K-Mean Clustering", font_size=36, color=WHITE)
        title.next_to(circle, DOWN)  # Align the title below the circle
        self.play(Write(title))

        # Add text "Created by Adam" below the title
        creator_text = Text("Created by: Aashkan Nikfarjam", font_size=24, color=GRAY)
        creator_text.next_to(title, DOWN)  # Position the creator text below the title
        self.play(Write(creator_text))

        self.wait()  # Wait for the animation to finish
        #####################
        #ploting graph
        #####################
        self.remove(creator_text,circle,title)
        # Create a set of random data points
        data_points = [np.array([random.uniform(-4, 4), random.uniform(-3, 3), 0]) for _ in range(20)]
        points = VGroup(*[Dot(point, radius=0.05, color=BLUE) for point in data_points])
        self.add(points)

        # Set the number of clusters
        num_clusters = 3

        # Initialize centroids randomly
        centroids = [np.array([random.uniform(-4, 4), random.uniform(-3, 3), 0]) for _ in range(num_clusters)]
        centroid_dots = VGroup(*[Dot(centroid, radius=0.1, color=RED) for centroid in centroids])
        self.add(centroid_dots)

        # Animate the K-Means clustering process
        for _ in range(5):
            self.play(AnimationGroup(*[centroid_dot.animate.move_to(centroid) for centroid_dot, centroid in zip(centroid_dots, centroids)]))
            clusters = [[] for _ in range(num_clusters)]
            for point in data_points:
                distances = [np.linalg.norm(point - centroid) for centroid in centroids]
                closest_cluster = np.argmin(distances)
                clusters[closest_cluster].append(point)

            new_centroids = [np.mean(cluster, axis=0) for cluster in clusters]
            centroids = new_centroids

        # Create convex hulls around the points in each cluster
        cluster_hulls = VGroup()
        for cluster in clusters:
            points_array = np.array(cluster)
            hull = ConvexHull(points_array[:, :2])
            hull_vertices = points_array[hull.vertices]
            hull_polygon = Polygon(*hull_vertices, color=YELLOW, fill_opacity=0.5)
            cluster_hulls.add(hull_polygon)

        # Label the final clusters
        cluster_labels = VGroup()
        for i, cluster in enumerate(clusters):
            cluster_points = VGroup(*[Dot(point, radius=0.05, color=GREEN) for point in cluster])
            cluster_label = Text(f"Cluster {i+1}", color=YELLOW).next_to(cluster_points, UP)
            cluster_labels.add(cluster_label)
            self.add(cluster_points)

        self.add(cluster_hulls)
        self.add(cluster_labels)
        self.wait()