import tensorflow as tf

# Define the input and output data
input_data = [[0,0], [0,1], [1,0], [1,1]]
output_data = [[0], [1], [1], [0]]

# Define the neural network architecture
model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(4, input_shape=(2,), activation='sigmoid'),
  tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(input_data, output_data, epochs=1000)

# Test the model
print(model.predict(input_data))
