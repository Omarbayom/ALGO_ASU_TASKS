import random

def find_fake_box(boxes):
    box_number = len(boxes)
    pieces_per_box = 50
    total_weight = sum(boxes)
    weight_of_real_metal = (total_weight + pieces_per_box) / (box_number * pieces_per_box)
    for i, weight in enumerate(boxes):
        if weight / pieces_per_box != weight_of_real_metal:
            return i + 1, weight, weight / pieces_per_box 

weight_of_real_metal = random.randint(2, 100)  
boxes = [weight_of_real_metal * 50 for _ in range(50)]  
fake_box_index = random.randint(0, 49)  
boxes[fake_box_index] = (weight_of_real_metal - 1) * 50  

fake_box_number, fake_box_weight, fake_piece_weight = find_fake_box(boxes)
print(f"The fake box is box number {fake_box_number}, with total weight {fake_box_weight} kg and each piece weighs {fake_piece_weight} kg")
print(f"The real weight of each piece is {weight_of_real_metal} kg")