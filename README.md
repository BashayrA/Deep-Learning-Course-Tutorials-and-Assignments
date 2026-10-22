# Deep Learning, Deeply Learned

Welcome to my repo for **Neural Networks & Deep Learning**.
This is where I keep all the tutorials and assignments, plus the proof that I made my GPU do some actual work instead of just playing games.

## What's inside

- **Tutorials**: weekly labs where I poke at tensors until they behave
- **Assignments**: the graded stuff, done with care and a reasonable amount of panic

## Built with

- Python
- PyTorch and TensorFlow (yes, both, I think I have FOMO)
- NumPy
- An RTX 4060 that has seen things

## Things I learned the hard way

- Rows are samples, columns are features. Always. Don't argue.
- A single neuron draws a straight line, no matter how hard you believe in it.
- If the loss goes down, that doesn't mean your code is right. Check your gradients.
- If you get an out-of-memory error, lower the batch size before you lower your expectations.
- ReLU is just `max(0, x)` and somehow it changed the world.

## Disclaimer

No neurons were harmed in the making of this repo.
A few were left permanently dead (ReLU's fault, not mine). 
![alt text](image.png)