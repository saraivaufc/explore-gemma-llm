import os
import keras
import tensorflow as tf
import keras_nlp

# Set the KERAS_BACKEND to 'jax'. You can also use 'torch' or 'tensorflow'.
os.environ["KERAS_BACKEND"] = "jax"  # JAX backend is preferred for its performance.

# Avoid memory fragmentation when using the JAX backend.
os.environ["XLA_PYTHON_CLIENT_MEM_FRACTION"]="1.00"

gemma_lm = keras_nlp.models.GemmaCausalLM.from_preset('./gemma_2b')

before_texts = ''

c='yes'
while c.lower() == 'yes':
    input_text = input('Me:')
    output_text = gemma_lm.generate(f'{before_texts}.\nMe:{input_text}', max_length=300)
    print('GPT:', output_text)
    before_texts += f'Me:{input_text}\nGPT:{output_text}'
    c = input('Do you like continue? (yes/no):')