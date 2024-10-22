class CropAndPad(meta.Augmenter):
    ...
    def _augment_keypoints(self, keypoints_on_images, random_state, parents, hooks):
        result = []
        nb_images = len(keypoints_on_images)
        rngs = random_state.duplicate(nb_images)
        for keypoints_on_image, rng in zip(keypoints_on_images, rngs):
            height, width = keypoints_on_image.shape[0:2]
            samples = self._draw_samples_image(rng, height, width)
            shifted = keypoints_on_image.shift(
                x=-samples.crop_left+samples.pad_left,
                y=-samples.crop_top+samples.pad_top)
            shifted.shape = samples.compute_new_shape(keypoints_on_image.shape)
            if self.keep_size:
                result.append(shifted.on(keypoints_on_image.shape))
            else:
                result.append(shifted)

        return result
    ...
