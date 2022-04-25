<template>
    <div class="photo_viewer">
        <h1> La photo vous convient-elle ?
        <img src="/photos/${name}" />
    </div>
</template>

<script>
export default {
    name: 'DisplayPhoto',
    props: {
        name: String
    }
}

</script>
