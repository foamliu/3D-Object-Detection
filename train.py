import argparse

import keras
import tensorflow as tf
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from keras.utils import multi_gpu_model

import migrate
from config import patience, batch_size, epochs, num_train_samples, num_valid_samples
from data_generator import train_gen, valid_gen
from model import build_encoder_decoder
from utils import custom_loss

if __name__ == '__main__':
    checkpoint_models_path = 'models/'

    # Callbacks
    tensor_board = keras.callbacks.TensorBoard(log_dir='./logs', histogram_freq=0, write_graph=True, write_images=True)
    model_names = checkpoint_models_path + 'model.{epoch:02d}-{val_loss:.4f}.hdf5'
    model_checkpoint = ModelCheckpoint(model_names, monitor='val_loss', verbose=1, save_best_only=True)
    early_stop = EarlyStopping('val_loss', patience=patience)
    reduce_lr = ReduceLROnPlateau('val_loss', factor=0.1, patience=int(patience / 4), verbose=1)

    model = build_encoder_decoder()
    migrate.migrate_model(model)

    model.compile(optimizer='nadam', loss=custom_loss)

    print(new_model.summary())

    # Summarize then go!
    num_cpu = get_available_cpus()
    workers = int(round(num_cpu / 2))
    print('num_gpu={}\nnum_cpu={}\nworkers={}\ntrained_models_path={}.'.format(num_gpu, num_cpu, workers,
                                                                               checkpoint_models_path))

    # Final callbacks
    callbacks = [tensor_board, model_checkpoint, early_stop, reduce_lr]

    # Start Fine-tuning
    new_model.fit_generator(train_gen(),
                            steps_per_epoch=num_train_samples // batch_size,
                            validation_data=valid_gen(),
                            validation_steps=num_valid_samples // batch_size,
                            epochs=epochs,
                            verbose=1,
                            callbacks=callbacks,
                            use_multiprocessing=True,
                            workers=workers
                            )
