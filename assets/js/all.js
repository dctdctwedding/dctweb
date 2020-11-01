// 畫面捲動時 navbar logo 縮小
$(function(){
	$(window).scroll(function(){
		if($(window).scrollTop() > 40){
      $('.navbar-brand .navbar-brand-img-center').css('width', '100px');
		} else {
      $('.navbar-brand .navbar-brand-img-center').css('width', '200px');
    }
    });
});

// popover
// $(function () {
//     $('[data-toggle="popover"]').popover();
// });


// emailjs
$("#surveySubmitId").click(function(){
    var surveyUserNameId = $("#surveyUserNameId").text();
    var surveyServiceId = $("#surveyServiceId").text();
    console.log(surveyUserNameId, surveyServiceId);
});
/*
function sendSurvey() {
    let template_params = {
        "userMail": "shooboost@gmail.com",
        "user": "麻糬麻糬",
    };
    emailjs.init("user_YM7dUJypL1Oog3Z6A0Clp");

    var service_id = "default_service";
    var template_id = "wedding_2020";
    emailjs.send(service_id, template_id, template_params);
    console.log("emailjs send")
}*/
// const submitBtn = document.querySelector('[data-action="submit"]');
const submitBtn = document.getElementById('surveySubmitId');
submitBtn.addEventListener("click", processFormData);
    function processFormData(e) {
        //取得 name 屬性為 form 的表單
        const form = document.forms['form'];
        //取 elements 集合中 name 屬性為 name 的值
        const UserName = form.elements.surveyUserNameId.value;
        const UserEmail = form.elements.surveyUserEmailId.value;
        const UserPhone = form.elements.surveyUserPhoneId.value;
        const Service = form.elements.surveyServiceId.value;
        const Date = form.elements.surveyDateId.value;
        const Type = form.elements.surveyTypeId.value;
        const Scenes = form.elements.surveyScenesId.value;
        const Location = form.elements.surveyLocationId.value;
        const UserVenue = form.elements.surveyUserVenueId.value;
        const Attendance = form.elements.surveyAttendanceId.value;
        const ChineseCeremony = form.elements.surveyChineseCeremonyId.value;
        const Bilingual = form.elements.surveyBilingualId.value;
        const InvitationCard = form.elements.surveyInvitationCardId.value;
        const UserSource = form.elements.surveyUserSourceId.value;
        const Progress = form.elements.surveyProgressId.value;
        const Submit = form.elements.surveySubmitId.value;

        let template_params = {
            "UserName": UserName,
            "UserEmail": UserEmail,
            "UserPhone": UserPhone,
            "Service": Service,
            "Date": Date,
            "Type": Type,
            "Scenes": Scenes,
            "Location": Location,
            "UserVenue": UserVenue,
            "Attendance": Attendance,
            "ChineseCeremony": ChineseCeremony,
            "Bilingual": Bilingual,
            "InvitationCard": InvitationCard,
            "UserSource": UserSource,
            "Progress": Progress,
            "Submit": Submit,
        };
        
        // 要使用再打開 yooo
        /**/
        emailjs.init("user_YM7dUJypL1Oog3Z6A0Clp");
    
        var service_id = "default_service";
        var template_id = "wedding_2020";
        emailjs.send(service_id, template_id, template_params);
        console.log("emailjs send");
        alert("成功寄出預約表單囉")
        
}
















