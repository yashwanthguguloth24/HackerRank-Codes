import itertools

n = input()
l = [(len(list(b)),int(a)) for a,b in itertools.groupby(n) ]
for i in range(len(l)):
    print(l[i],end = ' ')

for l in range(L):
        # Moving average of the gradients. Inputs: "v, grads, beta1". Output: "v".
        ### START CODE HERE ### (approx. 2 lines)
        v["dW" + str(l+1)] = (beta1*v["dW" + str(l+1)])+((1-beta1)*grads['dW' + str(l+1)])
        v["db" + str(l+1)] = (beta1*v["db" + str(l+1)])+((1-beta1)*grads['db' + str(l+1)])
        ### END CODE HERE ###

        # Compute bias-corrected first moment estimate. Inputs: "v, beta1, t". Output: "v_corrected".
        ### START CODE HERE ### (approx. 2 lines)
        v_corrected["dW" + str(l+1)] = v["dW" + str(l+1)]/(1-((beta1)**t))
        v_corrected["db" + str(l+1)] = v["db" + str(l+1)]/(1-((beta1)**t))
        ### END CODE HERE ###

        # Moving average of the squared gradients. Inputs: "s, grads, beta2". Output: "s".
        ### START CODE HERE ### (approx. 2 lines)
        s["dW" + str(l+1)] = (beta2*s["dW" + str(l+1)])+((1-beta2)*(grads['dW' + str(l+1)]**2))
        s["db" + str(l+1)] = (beta2*s["db" + str(l+1)])+((1-beta2)*(grads['db' + str(l+1)]**2))
        ### END CODE HERE ###

        # Compute bias-corrected second raw moment estimate. Inputs: "s, beta2, t". Output: "s_corrected".
        ### START CODE HERE ### (approx. 2 lines)
        s_corrected["dW" + str(l+1)] = s["dW" + str(l+1)]/(1-((beta2)**t))
        s_corrected["db" + str(l+1)] = s["db" + str(l+1)]/(1-((beta2)**t))
        ### END CODE HERE ###

        # Update parameters. Inputs: "parameters, learning_rate, v_corrected, s_corrected, epsilon". Output: "parameters".
        ### START CODE HERE ### (approx. 2 lines)
        parameters["W" + str(l+1)] = parameters["W" + str(l+1)] - (learning_rate)*(v_corrected["dW" + str(l+1)]/(np.sqrt(s_corrected["dW" + str(l+1)])+epsilon))
        parameters["b" + str(l+1)] = parameters["b" + str(l+1)] - (learning_rate)*(v_corrected["db" + str(l+1)]/(np.sqrt(s_corrected["db" + str(l+1)])+epsilon))
        ### END CODE HERE ###
