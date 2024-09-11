from faker import Faker


faker = Faker()  # Adding seed to persist the results

Faker.seed(0)

print(faker.name())
print(faker.name())
print(faker.name())
print(faker.name())
