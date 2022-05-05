<template>
    <div id="page">
        <h2>Voici votre photo !!!</h2>
        <img :src="'http://localhost:5000/photos/' + photoPath" alt="votre photo qui veut pas s'afficher">
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ConfirmPhotoView',
  props: ['photoPath'],
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/getconfs/confirm_photo';
      axios.get(path)
        .then((res) => {
          this.message = res.data.message;
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
