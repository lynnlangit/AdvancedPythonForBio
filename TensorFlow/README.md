# To verify your version of TensorFlow
# run this command from terminal

# NOTE: samples are from the main TensorFlow site at https://www.tensorflow.org

python -c 'import tensorflow as tf; print(tf.__version__)'  # for Python 2

# To fix the 'could speed up' error

To be compatible with as wide a range of machines as possible, TensorFlow defaults to only using SSE4.1 SIMD instructions on x86 machines. Most modern PCs and Macs support more advanced instructions, so if you're building a binary that you'll only be running on your own machine, you can enable these by using --copt=-march=native in your bazel build command.