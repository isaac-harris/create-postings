import random
import time
import csv

def get_text_file(filename):
  with open(filename, "r") as f:
    array = []
    for line in f:
      array.append(line)
  return array

name_list = get_text_file("names.txt")
industry_list = get_text_file("industries.txt")
country_list = get_text_file("countries.txt")
tag_list = get_text_file("tags.txt")

def get_fullname():
  return random.choice(name_list).strip() + " " + random.choice(name_list).strip()

def get_industry():
  return random.choice(industry_list).strip()

def get_tag():
  return random.choice(tag_list).strip()

def get_country_and_coords():
  country_array = random.choice(country_list).split(",")
  if len(country_array) != 4:
    return get_country_and_coords()
  return [country_array[0], country_array[2], country_array[3].strip()]

def generate_random_posting():
  name = get_fullname()

  business_slider = str(float(random.randint(0,8)) / 8) #random number from 0 - 1 in 0.125 increments
  brand_slider = str(float(random.randint(0,8)) / 8)
  influencer_slider = str(float(random.randint(0,8)) / 8)
  individual_slider = str(float(random.randint(0,8)) / 8)

  opportunity_type = random.choice(["Test","Review","Shout Out", "Product Placement"])
  opportunity_slider = str(float(random.randint(4,8)) / 8) #random number from 0.5 - 1 in 0.125 increments

  country_and_coords = get_country_and_coords()
  country = country_and_coords[0]
  country_slider = str(float(random.randint(4,8)) / 8)

  latitude = country_and_coords[1]
  longitude = country_and_coords[2]

  radius = str(random.randint(1, 3000))

  industry_type = get_industry()
  industry_slider = str(float(random.randint(4,8)) / 8)

  num_tags = random.randint(1,3)
  tag1_slider = str(float(random.randint(4,8)) / 8)
  tag2_slider = str(float(random.randint(4,8)) / 8)
  tag3_slider = str(float(random.randint(4,8)) / 8)

  tag1 = random.choice(tag_list).strip()

  tag2 = random.choice(tag_list).strip()
  while tag1 == tag2:
    print("tag2 repeated")
    tag2 = random.choice(tag_list)

  tag3 = random.choice(tag_list).strip()
  while tag1 == tag3 or tag2 == tag3:
    print("tag3 repeated")
    tag3 = random.choice(tag_list).strip()

  if num_tags <= 2:
    tag3 = ""
    tag3_slider = ""
  if num_tags <= 1:
    tag2 = ""
    tag2_slider = ""

  return [name, business_slider, brand_slider, influencer_slider, individual_slider, opportunity_type, opportunity_slider, country, country_slider, latitude, longitude, radius, industry_type, industry_slider, tag1, tag1_slider, tag2, tag2_slider, tag3, tag3_slider]

with open("posted_listings.txt", mode="w") as listing_file:
  listing_writer = csv.writer(listing_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

  num_elements = int(input("How many postings: "))

  for i in range(0,num_elements):
    listing_writer.writerow(generate_random_posting())
