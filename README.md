# Multiple time series alignments using penalized splines

## Description

This repository implements a model-based time series alignment method, using time-warping. Intuitively, this method is able to find the average across a set of time series data points, under the assumption that data samples may be phase shifted or time-warped relative to each other. The method outputs a data "centroid", as well as the time warping function for each sample to align with the centroid. The centroid as well as the time warping function for each sample is modeled using penalized Basis splines. A negative log-likelihood loss is used is used to learn the alignment. For demonstration, we used a Poisson point process likelihood, but the code is flexible enough to use different choices of loss functions. We applied the method to align simulated Poisson process data, and were able to recover the time warping functions used to misalign the data during simulation.

## File Structure

## Getting Started

* ```main.py```: Main entry point. Contains code to run the method on simulated data. Contains the main source code for the causal, temporal convolutional neural network, and the negative log-likelihood loss function.
* ```general_functions.py```: Includes utility and helper functions for the model, such as logging and plotting functions.
* ```TimeSeriesAlignmentModel.py```: Contains the main source code to run the alignment on the sample of time series data. As our current usecase is for point process time series data, the model is fit using a Poisson point process negative log-likelihood as its loss.
* ```test_gradients_with_timewarping.py```: Contains script to demonstrate the time-warping capabilities of the model.

### Prerequisites

```
      - Python 3.8 or higher
      - allensdk==2.15.1
      - cython==0.29.35
      - distro==1.8.0
      - h5py==3.8.0
      - hdmf==3.4.7
      - matplotlib==3.4.2
      - numpy==1.23.5
      - pandas==1.5.3
      - scipy==1.10.1
      - seaborn==0.12.2
      - torch==2.2.1
```

### Installation

1. Clone the repository:

```
git clone https://github.com/Tolani-O/Multiple_time_series_alignment_using_penalized_splines.git
cd Multiple_time_series_alignment_using_penalized_splines
```

2. Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```
pip install -r requirements.txt
```

### Usage

Simply run ```main.py```.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any feature additions or bug fixes.

## License

This project does not have a license at this moment.

## Contact

For any questions or issues, please open an issue on this repository or contact the repository owner at [Tolani-O](https://github.com/Tolani-O).

## Version History

* 0.1
    * Initial Release
