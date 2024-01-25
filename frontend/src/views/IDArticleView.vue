<template>
  <el-button type="primary" @click="edit = !edit">edit</el-button>
  <el-button type="success">save</el-button>
  <MdEditor v-model="text" v-if="edit" />
  <div v-else>
    <MdPreview :editorId="id" :modelValue="text" />

    <div class="right-top">
      <MdCatalog
        :editorId="id"
        :scrollElement="scrollElement"
        :previewTheme="ref(cyanosis)"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { MdPreview, MdEditor, MdCatalog } from 'md-editor-v3'
// preview.css相比style.css少了编辑器那部分样式
// import 'md-editor-v3/lib/preview.css'
import 'md-editor-v3/lib/style.css'

let edit = ref(false)
const id = 'preview-only'
const text = ref(`# Hello Editor 
# Hello Editor
## Hello Editor
### Hello Editor`)
const scrollElement = document.documentElement
</script>

<style scoped>
.right-top {
  position: fixed;
  top: 60px;
  right: 0;
  overflow: auto; /* 使用滚动条来处理超出视口的内容 */
  max-height: 100vh; /* 最大高度不超过视口高度 */
  width: 300px; /* 设置固定宽度，可以根据需要调整 */
  padding: 10px; /* 可以添加一些内边距以确保内容不贴紧边缘 */
  background-color: white; /* 设置背景色，以防内容透明时看不清 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* 添加阴影效果，提高可读性 */
  z-index: 1000; /* 确保组件在其他元素上方 */
  word-wrap: break-word; /* 允许在单词内换行 */
  overflow-wrap: break-word; /* 允许在单词内换行（兼容性更好的属性名） */
  white-space: normal; /* 允许文本自动换行 */
}
</style>
