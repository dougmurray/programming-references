import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def adc_code_to_volt(data, vref, gain=1):
    """Transfer function of ADC input to voltage, legacy."""
    adc_vin = (vref / 0xFFFF) / gain
    return adc_vin


def load_process_adc_data(input_file_name, output_file_name, vref=8.192, gain=2, Fs=12.288e6):
    """Takes a txt data file and makes a csv file with adc voltage conversion.
    Returns time and adc voltage data.
    Default vref, gain,  and sampling freq is based on specific ADC.
    Also assumes data files are in a folder at ./data.
    """
    data = np.loadtxt(f'data/{input_file_name}.txt')
    data *= adc_code_to_volt(data, vref, gain)
    time = np.arange(len(data)) / Fs
    df = pd.DataFrame({"time" : time, "data" : data})
    df.to_csv(f'data/{output_file_name}.csv', index=False)
    return time, data


def psd_helper_with_data_output(data, output_file_name, Fs=12.288e6):
    """Power Spectral Density with output csv file.
    Returns freqs, psd.
    Default sampling frequency (Fs) is based on specific ADC.
    Also assumes data files are in a folder at ./data.
    """
    freqs, psd = tl_psd.psd.powerSpectralDensity(data,Fs)
    freqs, psd = tl_psd.psd.logBin(freqs, psd)
    df = pd.DataFrame({"frequency" : freqs, "psd" : psd})
    df.to_csv(f'data/{output_file_name}.csv', index=False)
    return freqs, psd
