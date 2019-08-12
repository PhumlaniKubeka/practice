{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'MyCalculator'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-86c602846702>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mMyCalculator\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0maddition\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mmultiply\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mtest_addition\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m     \u001b[0;32massert\u001b[0m \u001b[0maddition\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m4\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m     \u001b[0;32massert\u001b[0m \u001b[0maddition\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m3\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m9\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'MyCalculator'"
     ]
    }
   ],
   "source": [
    "from MyCalculator import addition,multiply\n",
    "\n",
    "def test_addition():\n",
    "    assert addition(2,2) == 4\n",
    "    assert addition(2, 3,4) == 9\n",
    "    assert addition(2,3,4,5) == 13\n",
    "\n",
    "\n",
    "def test_multiplyy():\n",
    "    assert multiply(2,3) == 6\n",
    "    assert multiply(2,3,4) == 24\n",
    "    assert multiply(2,3,4,5) == 120"
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
