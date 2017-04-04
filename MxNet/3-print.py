import matplotlib.pyplot as plt
for i in range(10):
    plt.subplot(1,10,i+1)
    plt.imshow(train_img[i], cmap='Greys_r') # train_img is not defined
    plt.axis('off')
plt.show()
print('label: %s' % (train_lbl[0:10],))