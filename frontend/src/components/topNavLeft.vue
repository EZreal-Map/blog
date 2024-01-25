<template>
  <div>
    <router-link class="top-nav" :to="{ name: 'home' }" active-class="active"
      >首页</router-link
    >
    <router-link
      class="top-nav"
      :to="{ name: 'articles' }"
      active-class="active"
      >时间归档</router-link
    >
    <router-link
      class="top-nav"
      :to="{ name: 'catogory' }"
      active-class="active"
      >分类</router-link
    >
  </div>
</template>
<script setup></script>
<style scoped>
.top-nav {
  display: inline-block;
  padding: 0 20px;
  font-size: 20px;
  color: #fff;
  text-decoration: none;
}
</style>
