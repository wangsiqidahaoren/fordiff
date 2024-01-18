def rescale_image(self, 
            image: np.ndarray, 
            scale: Union[float, int]
            ) -> np.ndarray:
    self._ensure_format_supported(image)
    return image * scal
def to_numpy_array(self, image,
                   rescale=None,
                   channel_first=True):
    ...
    if rescale:
        image = self.rescale_image(
            image.astype(np.float32),
            1 / 255.0)
    ...