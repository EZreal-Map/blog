<!-- NotFoundView.vue -->
<template>
  <div>
    <h1>404 - Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
    <button @click="redirectToHome">Go to Home</button>
  </div>
</template>

<script>
export default {
  name: 'NotFoundView',
  methods: {
    redirectToHome() {
      // 在此处添加导航到首页的逻辑
      this.$router.push({ name: 'home' })
    }
  }
}
</script>

<style scoped>
/* 可以添加样式，使其更加美观 */
</style>
