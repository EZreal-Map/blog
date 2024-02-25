<template>
  <div class="container">
    <div class="title-select-container">
      <!-- 创建文章--title-->
      <el-input
        v-model="create_title"
        style="font-size: 16px; height: 40px"
        placeholder="请输入一个标题"
        clearable
      />
      <!-- 创建文章--tag-->
      <el-select
        v-model="create_tag_id"
        placeholder="请选择一个标签"
        size="large"
        style="width: 200px"
        filterable
        allow-create
      >
        <el-option
          v-for="tag in tags"
          :key="tag.id"
          :label="tag.name"
          :value="tag.id"
        />
      </el-select>
    </div>
    <!-- 创建文章--content-->
    <MdEditor
      style="height: 100%"
      @onSave="props.blog_id ? blogSave() : blogCreate()"
      v-model="create_content"
      @onUploadImg="onUploadImg"
    />
  </div>
</template>

<script setup>
import { MdEditor } from 'md-editor-v3'
import { postBlogService, putBlogIDService } from '@/api/blog.js'
// preview.css相比style.css少了编辑器那部分样式
// import 'md-editor-v3/lib/preview.css'
import 'md-editor-v3/lib/style.css'
import { ref, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
// import { ElMessage } from 'element-plus'
import { getTagListService } from '@/api/tag.js'
import { useUserStore } from '@/stores/user.js'
import { postUploadImgService } from '@/api/image'

const userState = useUserStore()
const router = useRouter()
const props = defineProps({
  blog_id: {
    type: String,
    default: null
  },
  title: {
    type: String,
    default: null
  },
  content: {
    type: String,
    default: null
  },
  tag_id: {
    type: Number,
    default: null
  }
})

const emit = defineEmits(['update:title', 'update:content', 'update:tag_id'])

const create_content = ref()
const create_title = ref()
const create_tag_id = ref()
const tags = ref()
;(async () => {
  const response = await getTagListService()
  // console.log('response:', response.data)
  tags.value = response.data
  console.log(props.tag_id)
  if (props.blog_id) {
    create_title.value = props.title
    create_content.value = props.content
    create_tag_id.value = props.tag_id
  }
})()

const blogCreate = async () => {
  if (!create_title.value || !create_content.value || !create_tag_id.value) {
    ElMessage({
      message: '请填写所有必填字段',
      type: 'warning'
    })
    return
  }
  console.log('blogCreate', props.blog_id)
  // create_tag_id.value保存的是已处在的tag_id，如果没有select匹配的tag_id，就保存input的tag_name
  const matchedTag = tags.value.find((tag) => tag.id === create_tag_id.value)
  const tagName = matchedTag ? matchedTag.name : create_tag_id.value
  const response = await postBlogService(
    create_title.value,
    create_content.value,
    tagName
  )
  // console.log(response)
  if (response.status === 200) {
    // console.log('blog save success')
    const id = response.data.id
    router.push({ path: `/blog/articles/${id}` })
    ElMessage({
      message: '新建博客成功',
      type: 'success'
    })
  }
}

const blogSave = async () => {
  console.log('blogSave', props.blog_id)
  const matchedTag = tags.value.find((tag) => tag.id === create_tag_id.value)
  const tagName = matchedTag ? matchedTag.name : create_tag_id.value
  const response = await putBlogIDService(
    props.blog_id,
    create_title.value,
    create_content.value,
    tagName
  )
  if (response.status === 200) {
    // console.log('blog save success')
    const id = response.data.id
    router.push({ path: `/blog/articles/${id}` })
    userState.Edit = false
    ElMessage({
      message: '修改博客成功',
      type: 'success'
    })
  }
}

const onUploadImg = async (files) => {
  // 上传图片计数
  let successfulUploadCount = 0

  // 使用 Promise.all 来等待所有上传完成
  await Promise.all(
    files.map(async (file) => {
      const form = new FormData()
      form.append('file', file)
      const response = await postUploadImgService(form)
      console.log('response:', response)

      if (response.status === 200) {
        const baseUrl = 'http://8.148.8.169'
        const imagesPortNumber = '8964'
        const imageMarkdown = `![${file.name}](${baseUrl}:${imagesPortNumber}/${encodeURIComponent(response.data.filename)})`
        // 将图片插入到编辑器中
        create_content.value = imageMarkdown + '\n' + create_content.value
        successfulUploadCount += 1
      }
    })
  )

  // 所有图片上传成功后显示消息
  if (successfulUploadCount === files.length) {
    ElMessage({
      message: '图片上传成功',
      type: 'success'
    })
  }
}

onUnmounted(() => {
  // 如果没有传入blog_id，就代表不是从create_button方法，则清空编辑器
  if (props.blog_id) {
    console.log('blog_id:', props.blog_id)
    emit('update:content', create_content.value)
    emit('update:title', create_title.value)
    // console.log(create_tag_id.value)
    emit('update:tag_id', create_tag_id.value)
  }
})
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  height: 100%;
}

/* 新增样式 */
.title-select-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-bottom: 16px;
  margin-top: 20px;
}

/* 调整 el-select 样式 */
.el-select {
  margin-left: 10px; /* 控制 el-select 与 el-input 之间的水平间距 */
}
</style>
