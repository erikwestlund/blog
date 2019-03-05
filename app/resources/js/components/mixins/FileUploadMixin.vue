<script>
    export default {
        data() {
            return {
                uploading: false,
            }
        },
        methods: {
            fileUpload($formData) {
                let formdata = new FormData();
                formdata.append('file', $formData);


                return axios.post('/admin/uploads', formdata, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
            },
            imageFileUpload($formData) {
                let formdata = new FormData();
                formdata.append('file', $formData);


                return axios.post('/admin/uploads/image', formdata, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
            },
        }
    }
</script>