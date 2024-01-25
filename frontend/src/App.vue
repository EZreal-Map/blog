<template>
  <div class="common-layout">
    <div class="header">
      <TopNavLeft></TopNavLeft>
      <TopNavRight></TopNavRight>
    </div>
    <div class="main">
      <router-view></router-view>
    </div>
  </div>
</template>
<script setup>
// import { ElContainer, ElHeader, ElAside, ElMain, ElFooter } from 'element-plus'
import TopNavLeft from '@/components/TopNavLeft.vue'
import TopNavRight from '@/components/TopNavRight.vue'

console.log('APP.vue')
</script>
<style scoped>
.common-layout {
  display: flex;
  flex-direction: column;
  height: 100vh;
  align-items: center; /* 水平居中 */
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #b3c0d1;
  height: 60px;
  width: 100%;
  flex-shrink: 0;
}

.main {
  flex: 1;
  background-color: #ccc;
  width: 1080px;
}
</style>
