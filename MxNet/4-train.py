import sys
import mxnet as mx
import logging

logging.getLogger().setLevel(logging.DEBUG)

model = mx.model.FeedForward(
    myData = 'data',
    myLabel = 'label',
    myGrad_Scale = '0',
    mlp = mx.symbol.SoftmaxOutput(data=myData,label=myLabel,grad_scale=myGrad_Scale),
    symbol = mlp,       # network structure -- ERROR 'mlp is not defined'
    num_epoch = 10,     # number of data passes for training 
    learning_rate = 0.1 # learning rate of SGD 
)
model.fit(
    X=train_iter,       # training data
    eval_data=val_iter, # validation data
    batch_end_callback = mx.callback.Speedometer(batch_size, 200) # output progress for each 200 data batches
)

# # from sample
#   act <- mx.symbol.Variable("data")
#   fc <- mx.symbol.FullyConnected(act, num.hidden = 10) 
#   act <- mx.symbol.Activation(data = fc, act_type = "relu")
#   fc <- mx.symbol.FullyConnected(act, num.hidden = 2)
#   mlp <- mx.symbol.SoftmaxOutput(fc)
#   set.seed(2015)

#   ############ sprials dataset ############

#   s <- sample(x = c("train", "test"), 
#               size = 1000, 
#               prob = c(.8,.2),
#               replace = TRUE)
  
#   dta <- mlbench.spirals(n = 1000, cycles = 1.2, sd = .03)
#   dta <- cbind(dta[["x"]], as.integer(dta[["classes"]]) - 1)
#   colnames(dta) <- c("x","y","label")
  
#   ######### train, validate, test ##########

#   dta.train <- dta[s == "train",]
#   dta.test <- dta[s == "test",]

#   ############# basic training #############

#   mx.set.seed(2014)
#   model <- mx.model.FeedForward.create(
#             symbol = mlp,
#             X = dta.train[, c("x", "y")], 
#             y = dta.train[, c("label")],
#             num.round = 5,
#             array.layout = "rowmajor",
#             learning.rate = 1,
#             eval.metric = mx.metric.accuracy)