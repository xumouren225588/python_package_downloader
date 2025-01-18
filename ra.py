import random
import os
def generate_random_string(length):
    letters_and_digits = [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]
    return ''.join(random.choices(letters_and_digits, k=length))
# 将环境变量写入到 $GITHUB_ENV
with open(os.environ.get('GITHUB_ENV'), 'a') as env_file:
    env_file.write(f"RA={generate_random_string(8)}\n")
