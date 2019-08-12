{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "945\n"
     ]
    }
   ],
   "source": [
    "def multiply(*args):\n",
    "    product = 1\n",
    "    for num in args:\n",
    "        product *= num\n",
    "    return product\n",
    "\n",
    "\n",
    "def addition(*args):\n",
    "    sum = 0\n",
    "    for num in args:\n",
    "        sum += num\n",
    "    return sum\n",
    "\n",
    "print(multiply(3,5,9,7))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
