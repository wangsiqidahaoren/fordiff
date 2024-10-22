class CropAndPad(meta.Augmenter):
    ...    
    def _augment_keypoints(self, keypoints_on_images, random_state, parents,
                           hooks):
        result = []
        nb_images = len(keypoints_on_images)
        rngs = random_state.duplicate(nb_images)
        for keypoints_on_image, rng in zip(keypoints_on_images, rngs):
            height, width = keypoints_on_image.shape[0:2]
            samples = self._draw_samples_image(rng, height, width)

            kpsoi_aug = _crop_and_pad_kpsoi(
                keypoints_on_image, croppings_img=samples.croppings,
                paddings_img=samples.paddings, keep_size=self.keep_size)
            result.append(kpsoi_aug)
    ...
def _crop_and_pad_kpsoi(kpsoi, croppings_img, paddings_img, keep_size):
    shifted = kpsoi.shift(
        x=-croppings_img[3]+paddings_img[3],
        y=-croppings_img[0]+paddings_img[0])
    shifted.shape = _compute_shape_after_crop_and_pad(
            kpsoi.shape, croppings_img, paddings_img)
    if keep_size:
        shifted = shifted.on(kpsoi.shape)
    return shifted