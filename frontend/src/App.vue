<template>
  <div class="layout">
    <!-- <div class="header"> -->
    <HeaderView class="layout-header"></HeaderView>
    <!-- </div> -->
    <div class="layout-main">
      <router-view></router-view>
    </div>
  </div>
</template>
<script setup>
console.log('APP.vue')
import HeaderView from '@/components/HeaderView.vue'
</script>
<style scoped>
.layout {
  display: flex;
  flex-direction: column;
  height: 100vh;
  align-items: center; /* 水平居中 */
  /* overflow-x: hidden; */
  /* width: 100vw; */
}

.layout-header {
  display: flex;
  /* justify-content: space-between; */
  /* align-items: center; */
  /* background-color: #add8e6; */
  /* height: 60px; */
  width: 100vw;
  /* flex-shrink: 0; */
  position: fixed;
  z-index: 1000;
  top: 0;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
.layout-main {
  margin-top: 60px;
  width: 1060px;
  min-height: calc(100vh - 60px); /* 设置高度为视口高度减去头部高度 */
  /* background-color: #f0f0f0; */
}
</style>
