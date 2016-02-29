#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-http
Version  : 1.0.2
Release  : 3
URL      : https://rubygems.org/downloads/http-1.0.2.gem
Source0  : https://rubygems.org/downloads/http-1.0.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-coveralls
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-docile
BuildRequires : rubygem-domain_name
BuildRequires : rubygem-http-cookie
BuildRequires : rubygem-http-form_data
BuildRequires : rubygem-mime-types
BuildRequires : rubygem-netrc
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rest-client
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-simplecov
BuildRequires : rubygem-simplecov-html
BuildRequires : rubygem-term-ansicolor
BuildRequires : rubygem-thor
BuildRequires : rubygem-tins
BuildRequires : rubygem-unf
BuildRequires : rubygem-unf_ext

%description
# ![http.rb](https://raw.github.com/httprb/http.rb/master/logo.png)
[![Gem Version](https://badge.fury.io/rb/http.svg)](https://rubygems.org/gems/http)
[![Build Status](https://secure.travis-ci.org/httprb/http.svg?branch=master)](https://travis-ci.org/httprb/http)
[![Code Climate](https://codeclimate.com/github/httprb/http.svg?branch=master)](https://codeclimate.com/github/httprb/http)
[![Coverage Status](https://coveralls.io/repos/httprb/http/badge.svg?branch=master)](https://coveralls.io/r/httprb/http)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/httprb/http/blob/master/LICENSE.txt)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n http-1.0.2
gem spec %{SOURCE0} -l --ruby > rubygem-http.gemspec

%build
gem build rubygem-http.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
http-1.0.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/http-1.0.2.gem
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/accept-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/auth-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/basic_auth-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/cdesc-Chainable.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/connect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/cookies-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/default_options%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/default_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/delete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/encoding-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/follow-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/get-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/head-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/nodelay-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/patch-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/persistent-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/post-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/put-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/through-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/trace-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Chainable/via-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Client/cdesc-Client.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Client/close-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Client/make_request_body-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Client/make_request_headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Client/make_request_uri-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Client/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Client/perform-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Client/request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Client/verify_connection%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Connection/cdesc-Connection.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Connection/close-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Connection/expired%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Connection/failed_proxy_connect%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Connection/finish_response-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Connection/keep_alive%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Connection/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Connection/read_headers%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Connection/read_more-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Connection/readpartial-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Connection/reset_timer-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Connection/send_proxy_connect_request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Connection/send_request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Connection/set_keep_alive-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Connection/start_tls-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/ConnectionError/cdesc-ConnectionError.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Error/cdesc-Error.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/%5b%5d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/%5b%5d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/%5b%5d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/Mixin/cdesc-Mixin.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/Mixin/headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/add-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/cdesc-Headers.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/coerce-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/delete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/each-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/get-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/initialize_copy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/keys-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/merge%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/merge-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/normalize_header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/set-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/to_a-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/to_h-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Headers/to_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/InvalidHeaderNameError/cdesc-InvalidHeaderNameError.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/MimeType/%5b%5d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/MimeType/Adapter/cdesc-Adapter.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/MimeType/JSON/cdesc-JSON.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/MimeType/JSON/decode-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/MimeType/JSON/encode-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/MimeType/cdesc-MimeType.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/MimeType/normalize-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/MimeType/register_adapter-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/MimeType/register_alias-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Options/%5b%5d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Options/OpenSSL/SSL/cdesc-SSL.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Options/OpenSSL/cdesc-OpenSSL.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Options/argument_error%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Options/cdesc-Options.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Options/def_option-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Options/default_socket_class-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Options/default_ssl_socket_class-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Options/default_timeout_class-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Options/defined_options-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Options/dup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Options/follow%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Options/merge-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Options/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Options/persistent%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Options/persistent%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Options/to_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Redirector/EndlessRedirectError/cdesc-EndlessRedirectError.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Redirector/TooManyRedirectsError/cdesc-TooManyRedirectsError.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Redirector/cdesc-Redirector.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Redirector/endless_loop%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Redirector/max_hops-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Redirector/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Redirector/perform-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Redirector/redirect_to-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Redirector/strict-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Redirector/too_many_hops%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/UnsupportedMethodError/cdesc-UnsupportedMethodError.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/UnsupportedSchemeError/cdesc-UnsupportedSchemeError.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/Writer/add_body_type_headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/Writer/add_headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/Writer/cdesc-Writer.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/Writer/connect_through_proxy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/Writer/join_headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/Writer/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/Writer/send_request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/Writer/stream-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/Writer/validate_body_type%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/Writer/write-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/body-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/cdesc-Request.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/connect_using_proxy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/default_host_header_value-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/headline-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/include_proxy_authorization_header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/normalize_uri-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/port-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/proxy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/proxy_authorization_header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/proxy_connect_header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/proxy_connect_headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/redirect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/scheme-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/socket_host-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/socket_port-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/stream-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/uri-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/using_authenticated_proxy%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/using_proxy%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/verb-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Request/version-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/RequestError/cdesc-RequestError.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Body/cdesc-Body.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Body/each-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Body/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Body/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Body/readpartial-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Body/stream%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Parser/%3c%3c-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Parser/add-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Parser/cdesc-Parser.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Parser/chunk-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Parser/finished%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Parser/headers%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Parser/headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Parser/http_version-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Parser/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Parser/on_body-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Parser/on_headers_complete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Parser/on_message_complete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Parser/reset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Parser/status_code-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Status/%5b%5d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Status/__getobj__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Status/__setobj__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Status/cdesc-Status.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Status/code-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Status/coerce-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Status/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Status/reason-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Status/symbolize-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Status/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/Status/to_sym-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/body-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/cdesc-Response.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/content_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/cookies-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/flush-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/parse-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/status-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/to_a-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Response/uri-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/ResponseError/cdesc-ResponseError.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/StateError/cdesc-StateError.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Global/%3c%3c-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Global/cdesc-Global.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Global/connect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Global/connect_ssl-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Global/log_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Global/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Global/perform_io-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Global/read_nonblock-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Global/readpartial-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Global/reset_counter-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Global/reset_timer-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Global/time_left-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Global/total_timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Global/wait_readable_or_timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Global/wait_writable_or_timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Global/write-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Global/write_nonblock-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Null/%3c%3c-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Null/cdesc-Null.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Null/connect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Null/connect_ssl-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Null/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Null/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Null/readpartial-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Null/rescue_readable-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Null/rescue_writable-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Null/socket-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Null/start_tls-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/Null/write-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/PerOperation/cdesc-PerOperation.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/PerOperation/connect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/PerOperation/connect_ssl-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/PerOperation/connect_timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/PerOperation/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/PerOperation/read_timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/PerOperation/readpartial-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/PerOperation/write-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/PerOperation/write_timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/Timeout/cdesc-Timeout.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/TimeoutError/cdesc-TimeoutError.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/URI/cdesc-URI.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/URI/http%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/URI/https%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/URI/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/HTTP/cdesc-HTTP.ri
/usr/lib64/ruby/gems/2.2.0/doc/http-1.0.2/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/.coveralls.yml
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/.rspec
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/.rubocop.yml
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/.travis.yml
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/.yardopts
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/CHANGES.md
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/Guardfile
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/LICENSE.txt
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/README.md
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/http.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/chainable.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/client.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/connection.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/content_type.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/errors.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/headers.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/headers/known.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/headers/mixin.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/mime_type.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/mime_type/adapter.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/mime_type/json.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/options.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/redirector.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/request.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/request/writer.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/response.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/response/body.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/response/parser.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/response/status.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/response/status/reasons.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/timeout/global.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/timeout/null.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/timeout/per_operation.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/uri.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/lib/http/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/logo.png
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http/client_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http/content_type_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http/headers/mixin_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http/headers_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http/options/body_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http/options/form_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http/options/headers_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http/options/json_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http/options/merge_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http/options/new_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http/options/proxy_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http/options_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http/redirector_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http/request/writer_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http/request_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http/response/body_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http/response/status_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http/response_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/lib/http_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/regression_specs.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/support/black_hole.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/support/capture_warning.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/support/dummy_server.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/support/dummy_server/servlet.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/support/http_handling_shared.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/support/proxy_server.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/support/servers/config.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/support/servers/runner.rb
/usr/lib64/ruby/gems/2.2.0/gems/http-1.0.2/spec/support/ssl_helper.rb
/usr/lib64/ruby/gems/2.2.0/specifications/http-1.0.2.gemspec
