<template>
  <div class="common-layout">
    <!-- <div class="header"> -->
    <HeaderView class="header"></HeaderView>
    <!-- </div> -->
    <div class="main">
      <router-view></router-view>
    </div>
  </div>
</template>
<script setup>
console.log('APP.vue')
import HeaderView from '@/components/HeaderView.vue'
</script>
<style scoped>
.common-layout {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100vw;
  align-items: center; /* 水平居中 */
  overflow-x: hidden;
}

.header {
  display: flex;
  /* justify-content: space-between; */
  /* align-items: center; */
  /* background-color: #b3c0d1; */
  /* height: 60px; */
  width: 100vw;
  /* flex-shrink: 0; */
  position: fixed;
  z-index: 1000;
  top: 0;
}
.main {
  margin-top: 60px;
  width: 60vw;
  min-width: 1080px;
  min-height: calc(100vh - 60px); /* 设置高度为视口高度减去头部高度 */
  background-color: #f0f0f0;
}
</style>
