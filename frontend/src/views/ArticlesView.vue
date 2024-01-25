<template>
  <div class="main">Articles</div>
  <!-- 跳转并携带params参数（to的对象写法） -->
  <RouterLink
    :to="{
      name: 'id-article', //用name跳转
      params: {
        id: 1209
      }
    }"
  >
    跳转文章详情
  </RouterLink>
</template>
<script setup>
console.log('Articles.vue')
</script>
<style scoped></style>
